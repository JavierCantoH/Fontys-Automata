# antlr -Dlanguage=Python3 NumericalExpression.g4 -visitor -o dist 
from antlr4 import *
from dist.NumericalExpressionLexer import NumericalExpressionLexer
from dist.NumericalExpressionParser import NumericalExpressionParser

def evaluate_and_print(argv):
  ast = parse_input_str(argv)
  result = evaluate_ast(ast)
  print(result)

def parse_input_str(argv):
    lexer = NumericalExpressionLexer(InputStream(argv))
    parser = NumericalExpressionParser(CommonTokenStream(lexer))
    # Parse the input string and return the AST
    return parser.numericalExpression()

def evaluate_ast(ast):
  if ast.getSymbolType() == NumericalExpressionParser.Number:
    # If the AST node is a number, return its value
    return int(ast.getText())
  elif ast.getSymbolType() == NumericalExpressionParser.VariableName:
    # If the AST node is a variable name, look up its value in the variable table
    variable_name = ast.getText()
    variable_value = variable_dictionary[variable_name]
    return variable_value
  elif ast.getSymbolType() == NumericalExpressionParser.mathematicalExpression:
    # If the AST node is a mathematical expression, recursively evaluate its subexpressions
    left = evaluate_ast(ast.getChild(0))
    operator = ast.getChild(1).getText()
    right = evaluate_ast(ast.getChild(2))

    if operator == '+':
      return left + right
    elif operator == '-':
      return left - right
    elif operator == '*':
      return left * right
    elif operator == '/':
      return left / right

variable_dictionary = {}

if __name__ == '__main__':    
    while True:
        print("New line: ", end='')
        argv = input()
        evaluate_and_print(argv)