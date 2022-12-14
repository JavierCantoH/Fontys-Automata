# antlr -Dlanguage=Python3 NumericalExpression.g4 -visitor -o dist 
from antlr4 import *
from dist.NumericalExpressionLexer import NumericalExpressionLexer
from dist.NumericalExpressionParser import NumericalExpressionParser
from dist.NumericalExpressionVisitor import NumericalExpressionVisitor

variable_dictionary = {}

class Evaluate(NumericalExpressionVisitor):
  
  def visitId(self, ctx:NumericalExpressionParser.IdContext):
    id = ctx.ID().getText()  
    if id in variable_dictionary:
      value = variable_dictionary[id]
      return value
    return 0
  
  def visitAssign(self, ctx:NumericalExpressionParser.AssignContext):
    id = ctx.ID().getText()
    value = self.visit(ctx.expr()) 
    variable_dictionary[id] = value
    return value
    
  def visitPrint(self, ctx:NumericalExpressionParser.PrintContext):
    value = self.visit(ctx.expr())
    print(value)
    return 0
     
  def visitInt(self, ctx:NumericalExpressionParser.IntContext):
    return int(ctx.getText())

  def visitParens(self, ctx:NumericalExpressionParser.ParensContext):
    return self.visit(ctx.expr())

  def visitOperation(self, ctx:NumericalExpressionParser.OperationContext):
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
        print('Divide by zero!')
        return 0
      return l / r

def main():
    input_stream = FileStream("input.txt")
    lexer = NumericalExpressionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NumericalExpressionParser(stream)
    tree = parser.prog()
    visitor = Evaluate()
    return visitor.visit(tree)

main()