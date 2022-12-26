# antlr -Dlanguage=Python3 MyGrammar.g4 -o dist 
import z3
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarListener import MyGrammarListener

class Evaluate(MyGrammarListener):
  def __init__(self):
    self.solver = z3.Solver()
    self.variables = {}

  def enterDeclaration(self, ctx):
    # Process a declaration
    var_name = ctx.ID().getText()
    # Add a Z3 Int variable to the solver
    self.variables[var_name] = z3.Int(var_name)
    self.solver.add(self.variables[var_name])

  def enterCheck_sat(self, ctx):
    # Check if the constraints are satisfiable
    print(self.solver.check())

  def enterGet_model(self, ctx):
    # Get a model for the constraints
    if self.solver.check() == z3.sat:
      print(self.solver.model())
    else:
      print("Unsatisfiable")

  def enterAssertion(self, ctx):
    # Process an assertion
    # Parse the constraint
    constraint = self.parse_constraint(ctx.constraint())
    # Add the constraint to the solver
    self.solver.add(constraint)

  def parse_constraint(self, ctx):
    """Recursively parses a constraint according to the grammar rules"""
    if ctx.DISTINCT():
      # Parse a distinct constraint
      var_names = [var.getText() for var in ctx.ID()]
      return z3.Distinct(*[self.variables[var] for var in var_names])
    elif ctx.AND():
      # Parse an and constraint
      constraint1 = self.parse_constraint(ctx.constraint(0))
      constraint2 = self.parse_constraint(ctx.constraint(1))
      return constraint1 and constraint2
    elif ctx.OR():
      # Parse an or constraint
      constraint1 = self.parse_constraint(ctx.constraint(0))
      constraint2 = self.parse_constraint(ctx.constraint(1))
      return constraint1 or constraint2
    elif ctx.GREATER():
      # Parse a greater than constraint
      var1 = ctx.ID(0).getText() if ctx.ID(0) else ctx.NUMBER(0).getText()
      var2 = ctx.ID(1).getText() if ctx.ID(1) else ctx.NUMBER(1).getText()
      if var1 in self.variables:
        var1 = self.variables[var1]
      else:
        var1 = z3.Int(var1)
      if var2 in self.variables:
        var2 = self.variables[var2]
      else:
        var2 = z3.Int(var2)
      return var1 > var2
    elif ctx.LESS():
      # Parse a less than constraint
      var1 = ctx.ID(0).getText() if ctx.ID(0) else ctx.NUMBER(0).getText()
      var2 = ctx.ID(1).getText() if ctx.ID(1) else ctx.NUMBER(1).getText()
      if var1 in self.variables:
        var1 = self.variables[var1]
      else:
        var1 = z3.Int(var1)
      if var2 in self.variables:
        var2 = self.variables[var2]
      else:
        var2 = z3.Int(var2)
      return var1 < var2
    elif ctx.GREATER_EQUAL():
      # Parse a greater equal than constraint
      var1 = ctx.ID(0).getText() if ctx.ID(0) else ctx.NUMBER(0).getText()
      var2 = ctx.ID(1).getText() if ctx.ID(1) else ctx.NUMBER(1).getText()
      if var1 in self.variables:
        var1 = self.variables[var1]
      else:
        var1 = z3.Int(var1)
      if var2 in self.variables:
        var2 = self.variables[var2]
      else:
        var2 = z3.Int(var2)
      return var1 >= var2
    elif ctx.LESS_EQUAL():
      # Parse a less equal than constraint
      var1 = ctx.ID(0).getText() if ctx.ID(0) else ctx.NUMBER(0).getText()
      var2 = ctx.ID(1).getText() if ctx.ID(1) else ctx.NUMBER(1).getText()
      if var1 in self.variables:
        var1 = self.variables[var1]
      else:
        var1 = z3.Int(var1)
      if var2 in self.variables:
        var2 = self.variables[var2]
      else:
        var2 = z3.Int(var2)
      return var1 <= var2
    elif ctx.BOOLEAN_EQUAL():
      # Parse an equal than constraint
      var1 = ctx.ID(0).getText() if ctx.ID(0) else ctx.NUMBER(0).getText()
      var2 = ctx.ID(1).getText() if ctx.ID(1) else ctx.NUMBER(1).getText()
      if var1 in self.variables:
        var1 = self.variables[var1]
      else:
        var1 = z3.Int(var1)
      if var2 in self.variables:
        var2 = self.variables[var2]
      else:
        var2 = z3.Int(var2)
      return var1 == var2

def main():
    input_stream = FileStream("input.txt")
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.prog()
    listener = Evaluate()
    walker = ParseTreeWalker().walk(listener, tree)
    return walker

main()