# antlr -Dlanguage=Python3 MyGrammar.g4 -visitor -o dist 
import sys
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor

class Evaluate(MyGrammarVisitor):
    def visitProgram(self, ctx:MyGrammarParser.ProgramContext):
        print()
        # # TODO
        # for i in ctx.getChildCount():
        #     if i == ctx.getChildCount() - 1:
        #         print()
        #     else:
        #         #prog.
    
    vars = []
    def visitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        id = ctx.ID().getText()
        if id in vars:
            print(id + "already declared.")
            return
        else:
            value = int(ctx.NUM().getText())
            newTuple = (id, value)
            vars.append(newTuple)
            return
    
    def visitVariable(self, ctx:MyGrammarParser.VariableContext):
        id = ctx.ID().getText()
        checkID = []
        checkValues = []
        index = 0
        for identifier, value in vars:
            checkID.append(identifier)
            checkValues.append(value)
            
        if id not in vars:
            print(id + "not declared.")
            return
        else:
            for i, ID in enumerate(checkID):
                if id == ID:
                    index = i
            for i, value in enumerate(checkValues):
                if i == index:
                    return int(value)
        
    def visitNumberExpr(self, ctx:MyGrammarParser.NumberContext):
        return int(ctx.getText())

    def visitParentExpr(self, ctx:MyGrammarParser.ParentExprContext):
        return self.visit(ctx.expr())

    def visitOperationExpr(self, ctx:MyGrammarParser.OperationExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r
 
def main(argv) -> float:
    input_stream = FileStream("input2.txt")
    #input_stream = InputStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.prog()
    visitor = Evaluate()
    return visitor.visit(tree)

if __name__ == '__main__':    
    #while True:
        #print("New line to evaluate: ", end='')
        #argv = input()
        #print(main(argv))
    print(main(sys.argv))