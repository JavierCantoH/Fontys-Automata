# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#prog.
    def enterProg(self, ctx:MyGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#prog.
    def exitProg(self, ctx:MyGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#printLine.
    def enterPrintLine(self, ctx:MyGrammarParser.PrintLineContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printLine.
    def exitPrintLine(self, ctx:MyGrammarParser.PrintLineContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#assign.
    def enterAssign(self, ctx:MyGrammarParser.AssignContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assign.
    def exitAssign(self, ctx:MyGrammarParser.AssignContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#blank.
    def enterBlank(self, ctx:MyGrammarParser.BlankContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#blank.
    def exitBlank(self, ctx:MyGrammarParser.BlankContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#printExpr.
    def enterPrintExpr(self, ctx:MyGrammarParser.PrintExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printExpr.
    def exitPrintExpr(self, ctx:MyGrammarParser.PrintExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#parens.
    def enterParens(self, ctx:MyGrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#parens.
    def exitParens(self, ctx:MyGrammarParser.ParensContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#id.
    def enterId(self, ctx:MyGrammarParser.IdContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#id.
    def exitId(self, ctx:MyGrammarParser.IdContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#operation.
    def enterOperation(self, ctx:MyGrammarParser.OperationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#operation.
    def exitOperation(self, ctx:MyGrammarParser.OperationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#int.
    def enterInt(self, ctx:MyGrammarParser.IntContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#int.
    def exitInt(self, ctx:MyGrammarParser.IntContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#print.
    def enterPrint(self, ctx:MyGrammarParser.PrintContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#print.
    def exitPrint(self, ctx:MyGrammarParser.PrintContext):
        pass



del MyGrammarParser