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
    return_type = ctx.TYPE().getText()
    name = ctx.ID().getText()
    params = []
    if ctx.formalParameters():
        for param in ctx.formalParameters().formalParameter():
            param_type = param.TYPE().getText()
            param_name = param.ID().getText()
            params.append((param_type, param_name))
    body = self.visit(ctx.block())
    return (return_type, name, params, body)
      
  def visitReturnFunc(self, ctx:MyGrammarParser.ReturnFuncContext):
    if ctx.expr():
        return ('return', self.visit(ctx.expr()))
    else:
        return ('return', None)
    
  def visitCallingFunc(self, ctx:MyGrammarParser.CallingFuncContext):
    return ('call', self.visit(ctx.expr()))
  
  def visitExprFuncCall(self, ctx:MyGrammarParser.ExprFuncCallContext):
    name = ctx.ID().getText()
    args = []
    if ctx.exprList():
        for expr in ctx.exprList().expr():
            args.append(self.visit(expr))
    return ('exprFuncCall', name, args)

  def visitBlock(self, ctx:MyGrammarParser.BlockContext):
    statements = []
    for statement in ctx.statement():
        statements.append(self.visit(statement))
    return statements

  def visitFormalParameters(self, ctx:MyGrammarParser.FormalParametersContext):
      params = []
      for param in ctx.formalParameter():
          param_type = param.TYPE().getText()
          param_name = param.ID().getText()
          params.append((param_type, param_name))
      return params

  def visitFormalParameter(self, ctx:MyGrammarParser.FormalParameterContext):
      param_type = ctx.TYPE().getText()
      param_name = ctx.ID().getText()
      return (param_type, param_name)
  
  def visitExprList(self, ctx:MyGrammarParser.ExprListContext):
    exprs = []
    for expr in ctx.expr():
        exprs.append(self.visit(expr))
    return exprs  
  
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