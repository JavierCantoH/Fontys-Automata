# Generated from NumericalExpression.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NumericalExpressionParser import NumericalExpressionParser
else:
    from NumericalExpressionParser import NumericalExpressionParser

# This class defines a complete generic visitor for a parse tree produced by NumericalExpressionParser.

class NumericalExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NumericalExpressionParser#numericalExpression.
    def visitNumericalExpression(self, ctx:NumericalExpressionParser.NumericalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#variableAssignment.
    def visitVariableAssignment(self, ctx:NumericalExpressionParser.VariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#printStatement.
    def visitPrintStatement(self, ctx:NumericalExpressionParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#mathematicalExpression.
    def visitMathematicalExpression(self, ctx:NumericalExpressionParser.MathematicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#operator.
    def visitOperator(self, ctx:NumericalExpressionParser.OperatorContext):
        return self.visitChildren(ctx)



del NumericalExpressionParser