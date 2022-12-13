# Generated from NumericalExpression.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NumericalExpressionParser import NumericalExpressionParser
else:
    from NumericalExpressionParser import NumericalExpressionParser

# This class defines a complete listener for a parse tree produced by NumericalExpressionParser.
class NumericalExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by NumericalExpressionParser#numericalExpression.
    def enterNumericalExpression(self, ctx:NumericalExpressionParser.NumericalExpressionContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#numericalExpression.
    def exitNumericalExpression(self, ctx:NumericalExpressionParser.NumericalExpressionContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#variableAssignment.
    def enterVariableAssignment(self, ctx:NumericalExpressionParser.VariableAssignmentContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#variableAssignment.
    def exitVariableAssignment(self, ctx:NumericalExpressionParser.VariableAssignmentContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#printStatement.
    def enterPrintStatement(self, ctx:NumericalExpressionParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#printStatement.
    def exitPrintStatement(self, ctx:NumericalExpressionParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#mathematicalExpression.
    def enterMathematicalExpression(self, ctx:NumericalExpressionParser.MathematicalExpressionContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#mathematicalExpression.
    def exitMathematicalExpression(self, ctx:NumericalExpressionParser.MathematicalExpressionContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#operator.
    def enterOperator(self, ctx:NumericalExpressionParser.OperatorContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#operator.
    def exitOperator(self, ctx:NumericalExpressionParser.OperatorContext):
        pass



del NumericalExpressionParser