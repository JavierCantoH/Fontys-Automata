# antlr -Dlanguage=Python3 MyGrammar2.g4 -o dist 
import z3
from antlr4 import *
from dist.MyGrammar2Lexer import MyGrammar2Lexer
from dist.MyGrammar2Parser import MyGrammar2Parser
from dist.MyGrammar2Listener import MyGrammar2Listener

class Evaluate(MyGrammar2Listener):
    def __init__(self):
        self.solver = z3.Solver()
        self.variables = {}
        self.assertions = []

    def enterDeclare_fun(self, ctx:MyGrammar2Parser.Declare_funContext):
        var_name = ctx.ID().getText()
        self.variables[var_name] = z3.Int(var_name)

    def enterAssert_cmd(self, ctx:MyGrammar2Parser.Assert_cmdContext):
        # Evaluate the formula and add it as an assertion to the solver
        formula = self.evaluate_formula(ctx.formula())
        self.assertions.append(formula)
        self.solver.add(formula)
    
    def evaluate_formula(self, ctx:MyGrammar2Parser.FormulaContext):
        if ctx.distinct_formula():
            # Handle distinct formula
            values = [self.evaluate_values(v) for v in ctx.distinct_formula().values()]
            return z3.Distinct(*values)
        elif ctx.comp():
            # Handle compound formula
            left = self.evaluate_formula(ctx.formula(0))
            right = self.evaluate_formula(ctx.formula(1))
            if ctx.comp().getText() == 'and':
                return z3.And(left, right)
            else:
                return z3.Or(left, right)
        elif ctx.comparator():
            # Handle comparator formula
            left = self.evaluate_values(ctx.values(0))
            right = self.evaluate_values(ctx.values(1))
            comparator = ctx.comparator().getText()
            if comparator == '>=':
                return left >= right
            elif comparator == '<=':
                return left <= right
            elif comparator == '<':
                return left < right
            elif comparator == '>':
                return left > right
            elif comparator == '=':
                return left == right
        else:
            # Handle values
            return self.evaluate_values(ctx.values())

    def evaluate_values(self, ctx:MyGrammar2Parser.ValuesContext):
        if ctx.ID():
            # Handle identifier
            id_text = ctx.ID().getText()
            if id_text in self.variables:
                # Return a function call if the identifier is a declared function
                return self.variables[id_text]
            else:
                raise ValueError(f"VAL: '{ctx.getText()}' not declared.")
        elif ctx.NUMBER():
            # Handle number
            return z3.Int(ctx.NUMBER().getText())

    def enterCheck_sat(self, ctx:MyGrammar2Parser.Check_satContext):
        # Check the satisfiability of the assertions
        result = self.solver.check()
        if result == z3.sat:
            print("Satisfiable")
        elif result == z3.unsat:
            print("Unsatisfiable")
        else:
            print("Unknown")
    
    def exitGet_model(self, ctx:MyGrammar2Parser.Get_modelContext):
        model = self.solver.model()
        for d in model.decls():
            print(f"{d.name()} = {model[d]}")

def main():
    input_stream = FileStream("sudokuA.txt")
    lexer = MyGrammar2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammar2Parser(stream)
    tree = parser.program()
    listener = Evaluate()
    walker = ParseTreeWalker().walk(listener, tree)
    return walker

main()