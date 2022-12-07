# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#Program.
    def enterProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#Program.
    def exitProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#Declaration.
    def enterDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#Declaration.
    def exitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#Variable.
    def enterVariable(self, ctx:MyGrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#Variable.
    def exitVariable(self, ctx:MyGrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#Number.
    def enterNumber(self, ctx:MyGrammarParser.NumberContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#Number.
    def exitNumber(self, ctx:MyGrammarParser.NumberContext):
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



del MyGrammarParser