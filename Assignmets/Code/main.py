# antlr -Dlanguage=Python3 MyGrammar.g4 -visitor -o dist 
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor

variable_dictionary = {}

# int sum(int x, int y){
#     double z = x + y;
#     return z;
# }

# sum(5, 10.5)

class Evaluate(MyGrammarVisitor):
  
  def visitFunctionDecl(self, ctx:MyGrammarParser.FunctionDeclContext):
    type = ctx.TYPE().getText()
    id = ctx.ID().getText()
    
    if type == 'int':
      self.visit(ctx.block())
    elif type == 'void':
    
    elif type == 'double':
      
  
  # def visitReturnFunc(self, ctx:MyGrammarParser.ReturnFuncContext):
  
  # def visitExprFuncCall(self, ctx:MyGrammarParser.ExprFuncCallContext):
    
  # def visitFormalParameters(self, ctx:MyGrammarParser.FormalParametersContext):
    
  # def visitFormalParameter(self, ctx:MyGrammarParser.FormalParameterContext):
  
  # def visitExprList(self, ctx:MyGrammarParser.ExprListContext):
  
  
  
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
    return None

  def visitAssignExpr(self, ctx:MyGrammarParser.AssignExprContext):
    id = ctx.ID().getText()
    if id in variable_dictionary:
      value = self.visit(ctx.expr()) 
      variable_dictionary[id] = value
    else:
      print("please specify the variable type")
  
  def visitAssign(self, ctx:MyGrammarParser.AssignContext):
    id = ctx.ID().getText()
    
    if ctx.EQUAL() and (ctx.TYPE().getText() == 'int' or ctx.TYPE().getText() == 'float'):
        value = self.visit(ctx.expr()) 
        variable_dictionary[id] = value
    else:
      variable_dictionary[id] = None
    return 0

  def visitPrint(self, ctx:MyGrammarParser.PrintContext):
    print(self.visitChildren(ctx))
    return self.visitChildren(ctx)
    
  def visitPrintLine(self, ctx:MyGrammarParser.PrintContext):
    value = self.visit(ctx.expr())
    #print(value)
    return 0
     
  def visitNumber(self, ctx:MyGrammarParser.NumberContext):
    if ctx.INT():
      return int(ctx.getText())
    else:
      return float(ctx.getText())

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