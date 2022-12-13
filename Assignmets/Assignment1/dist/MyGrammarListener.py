# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#numericalExpression.
    def enterNumericalExpression(self, ctx:MyGrammarParser.NumericalExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#numericalExpression.
    def exitNumericalExpression(self, ctx:MyGrammarParser.NumericalExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#variableAssignment.
    def enterVariableAssignment(self, ctx:MyGrammarParser.VariableAssignmentContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#variableAssignment.
    def exitVariableAssignment(self, ctx:MyGrammarParser.VariableAssignmentContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#printStatement.
    def enterPrintStatement(self, ctx:MyGrammarParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printStatement.
    def exitPrintStatement(self, ctx:MyGrammarParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#mathematicalExpression.
    def enterMathematicalExpression(self, ctx:MyGrammarParser.MathematicalExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#mathematicalExpression.
    def exitMathematicalExpression(self, ctx:MyGrammarParser.MathematicalExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#operator.
    def enterOperator(self, ctx:MyGrammarParser.OperatorContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#operator.
    def exitOperator(self, ctx:MyGrammarParser.OperatorContext):
        pass



del MyGrammarParser