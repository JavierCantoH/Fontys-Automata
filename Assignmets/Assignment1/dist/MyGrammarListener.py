# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#NumberExpr.
    def enterNumberExpr(self, ctx:MyGrammarParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#NumberExpr.
    def exitNumberExpr(self, ctx:MyGrammarParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#OperationExpr.
    def enterOperationExpr(self, ctx:MyGrammarParser.OperationExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#OperationExpr.
    def exitOperationExpr(self, ctx:MyGrammarParser.OperationExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#ParentExpr.
    def enterParentExpr(self, ctx:MyGrammarParser.ParentExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#ParentExpr.
    def exitParentExpr(self, ctx:MyGrammarParser.ParentExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#VariableExpr.
    def enterVariableExpr(self, ctx:MyGrammarParser.VariableExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#VariableExpr.
    def exitVariableExpr(self, ctx:MyGrammarParser.VariableExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#VariableAssignExpr.
    def enterVariableAssignExpr(self, ctx:MyGrammarParser.VariableAssignExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#VariableAssignExpr.
    def exitVariableAssignExpr(self, ctx:MyGrammarParser.VariableAssignExprContext):
        pass



del MyGrammarParser