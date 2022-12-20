# antlr -Dlanguage=Python3 MyGrammar.g4 -visitor -o dist 
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor

variable_dictionary = {}

class Evaluate(MyGrammarVisitor):
  
  def visitText(self, ctx:MyGrammarParser.TextContext):
    return ctx.getText()
  
  def visitLoop(self, ctx:MyGrammarParser.LoopContext):
    condition = self.visit(ctx.expr())
    while condition:
        self.visit(ctx.statement())
        condition = self.visit(ctx.expr())
  
  def visitIfStat(self, ctx:MyGrammarParser.IfStatContext):
    if self.visit(ctx.expr()) == True:
      self.visit(ctx.statement(0))
    elif ctx.ELSE():
      self.visit(ctx.statement(1))
  
  def visitId(self, ctx:MyGrammarParser.IdContext):
    id = ctx.ID().getText()  
    if id in variable_dictionary:
      value = variable_dictionary[id]
      return value
    return 0
  
  def visitAssign(self, ctx:MyGrammarParser.AssignContext):
    id = ctx.ID().getText()
    value = self.visit(ctx.expr()) 
    variable_dictionary[id] = value
    return value

  def visitPrint(self, ctx:MyGrammarParser.PrintContext):
    print(self.visitChildren(ctx))
    return self.visitChildren(ctx)
    
  def visitPrintLine(self, ctx:MyGrammarParser.PrintContext):
    value = self.visit(ctx.expr())
    #print(value)
    return 0
     
  def visitInt(self, ctx:MyGrammarParser.IntContext):
    return int(ctx.getText())

  def visitParens(self, ctx:MyGrammarParser.ParensContext):
    return self.visit(ctx.expr())

  def visitOperation(self, ctx:MyGrammarParser.OperationContext):
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
    elif op == 'and':
      return l and r
    elif op == 'or':
      return l or r
    elif op == '>':
      return l > r
    elif op == '<':
      return l < r
    elif op == '>=':
      return l >= r
    elif op == '<=':
      return l <= r
    elif op == '!=':
      return l != r
    elif op == '==':
      return l == r

def main():
    input_stream = FileStream("input.txt")
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.prog()
    visitor = Evaluate()
    return visitor.visit(tree)

main()