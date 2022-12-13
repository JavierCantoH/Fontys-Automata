# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#numericalExpression.
    def visitNumericalExpression(self, ctx:MyGrammarParser.NumericalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#variableAssignment.
    def visitVariableAssignment(self, ctx:MyGrammarParser.VariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#printStatement.
    def visitPrintStatement(self, ctx:MyGrammarParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#mathematicalExpression.
    def visitMathematicalExpression(self, ctx:MyGrammarParser.MathematicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#operator.
    def visitOperator(self, ctx:MyGrammarParser.OperatorContext):
        return self.visitChildren(ctx)



del MyGrammarParser