# antlr -Dlanguage=Python3 MyGrammar.g4 -visitor -o dist 
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor

variable_dictionary = {}

class Evaluate(MyGrammarVisitor):
  
  def visitFunctionDecl(self, ctx:MyGrammarParser.FunctionDeclContext):
    func_name = ctx.ID().getText()
    if func_name in variable_dictionary:
      raise Exception(f"Function {func_name} already defined")
    else:
      variable_dictionary[func_name] = ctx
    return self.visit(ctx.block())

  def visitCallingFunc(self, ctx:MyGrammarParser.CallingFuncContext):
    func_name = ctx.ID().getText()
    if func_name in variable_dictionary:
      func_decl = variable_dictionary[func_name]
      func_args = self.visit(func_decl.formalParameters())
      provided_args = self.visit(ctx.exprList())
      if len(func_args) == len(provided_args):
        for i in range(len(func_args)):
          arg_name = func_args[i].ID().getText()
          arg_value = provided_args[i]
          variable_dictionary[arg_name] = arg_value
        return self.visit(ctx.block())
      else:
        raise Exception(f"Function {func_name} expects {len(func_args)} arguments, but {len(provided_args)} were provided")
    else:
      raise Exception(f"Function {func_name} is not defined")
  
  def visitReturnFunc(self, ctx:MyGrammarParser.ReturnFuncContext):
    if ctx.expr():
      return self.visit(ctx.expr()) 
    else:
      return None

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
    else:
      raise Exception(f"Identifier {id} is not defined")

  def visitAssignExpr(self, ctx:MyGrammarParser.AssignExprContext):
    id = ctx.ID().getText()
    if id in variable_dictionary:
      value = self.visit(ctx.expr()) 
      variable_dictionary[id] = value
    else:
      print("Please specify the variable type")
  
  def visitAssign(self, ctx:MyGrammarParser.AssignContext):
    id = ctx.ID().getText()
    if ctx.TYPE().getText() == 'int':
      if ctx.EQUAL():
        value = self.visit(ctx.expr())
        variable_dictionary[id] = value
      else:
        variable_dictionary[id] = 0
    elif ctx.TYPE().getText() == 'float':
      if ctx.EQUAL():
        value = self.visit(ctx.expr())
        variable_dictionary[id] = value
      else:
        variable_dictionary[id] = 0.0
    else:
      raise Exception(f"Unsupported type {ctx.TYPE().getText()}")

  def visitPrint(self, ctx:MyGrammarParser.PrintContext):
    # print(self.visitChildren(ctx))
    # return self.visitChildren(ctx)
    value = self.visit(ctx.expr())
    print(value)
    return value
    
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