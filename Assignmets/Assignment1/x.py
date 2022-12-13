# antlr -Dlanguage=Python3 NumericalExpression.g4 -visitor -o dist 
import sys
from antlr4 import *
from antlr4 import Parser
from antlr4.ParserRuleContext import getSymbolType

from dist.NumericalExpressionLexer import NumericalExpressionLexer
from dist.NumericalExpressionParser import NumericalExpressionParser

def evaluate_and_print(argv):
  # Parse the input string to build the AST
  ast = parse_input_str(argv)

  # Evaluate the AST to get the result of the numerical expression
  result = evaluate_ast(ast)

  # Print the result
  print(result)


# Define the parse_input_str() function
def parse_input_str(argv):
    
    #input_stream = FileStream("input2.txt")
    input_ = InputStream(argv)
    
    # Create a lexer to tokenize the input string
    #lexer = NumericalExpressionLexer(input_stream)
    #stream = CommonTokenStream(lexer)
    # Create a parser to build the AST from the tokens
    #parser = NumericalExpressionParser(stream)
    
    
    # Create a lexer to tokenize the input string
    lexer = NumericalExpressionLexer(input_)
    # Create a parser to build the AST from the tokens
    parser = NumericalExpressionParser(CommonTokenStream(lexer))
    # Parse the input string and return the AST
    return parser.numericalExpression()

def evaluate_ast(ast):
  # Check the type of the AST node
  if ast.getSymbolType() == NumericalExpressionParser.Number:
    # If the AST node is a number, return its value
    return int(ast.getText())
  elif ast.getSymbolType() == NumericalExpressionParser.VariableName:
    # If the AST node is a variable name, look up its value in the variable table
    variable_name = ast.getText()
    variable_value = variable_table[variable_name]
    return variable_value
  elif ast.getSymbolType() == NumericalExpressionParser.mathematicalExpression:
    # If the AST node is a mathematical expression, recursively evaluate its subexpressions
    left_operand = evaluate_ast(ast.getChild(0))
    operator = ast.getChild(1).getText()
    right_operand = evaluate_ast(ast.getChild(2))

    # Perform the operation specified by the operator
    if operator == '+':
      return left_operand + right_operand
    elif operator == '-':
      return left_operand - right_operand
    elif operator == '*':
      return left_operand * right_operand
    elif operator == '/':
      return left_operand / right_operand

# Create an empty dictionary to store the values of variables
variable_table = {}

if __name__ == '__main__':    
    while True:
        print("New line to evaluate: ", end='')
        argv = input()
        evaluate_and_print(argv)
        #print(main(argv))
        


# from antlr4 import InputStream

# # Create an InputStream object
# input_stream = InputStream("Some input")

# # Convert the InputStream to a list
# input_list = list(input_stream)

# # Iterate over the list
# for item in input_list:
#     print(item)
