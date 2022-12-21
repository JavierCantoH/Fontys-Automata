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


    # Enter a parse tree produced by MyGrammarParser#assignExpr.
    def enterAssignExpr(self, ctx:MyGrammarParser.AssignExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assignExpr.
    def exitAssignExpr(self, ctx:MyGrammarParser.AssignExprContext):
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


    # Enter a parse tree produced by MyGrammarParser#ifExpr.
    def enterIfExpr(self, ctx:MyGrammarParser.IfExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#ifExpr.
    def exitIfExpr(self, ctx:MyGrammarParser.IfExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#loopExpr.
    def enterLoopExpr(self, ctx:MyGrammarParser.LoopExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#loopExpr.
    def exitLoopExpr(self, ctx:MyGrammarParser.LoopExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#number.
    def enterNumber(self, ctx:MyGrammarParser.NumberContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#number.
    def exitNumber(self, ctx:MyGrammarParser.NumberContext):
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


    # Enter a parse tree produced by MyGrammarParser#text.
    def enterText(self, ctx:MyGrammarParser.TextContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#text.
    def exitText(self, ctx:MyGrammarParser.TextContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#operation.
    def enterOperation(self, ctx:MyGrammarParser.OperationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#operation.
    def exitOperation(self, ctx:MyGrammarParser.OperationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#print.
    def enterPrint(self, ctx:MyGrammarParser.PrintContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#print.
    def exitPrint(self, ctx:MyGrammarParser.PrintContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#loop.
    def enterLoop(self, ctx:MyGrammarParser.LoopContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#loop.
    def exitLoop(self, ctx:MyGrammarParser.LoopContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#ifStat.
    def enterIfStat(self, ctx:MyGrammarParser.IfStatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#ifStat.
    def exitIfStat(self, ctx:MyGrammarParser.IfStatContext):
        pass



del MyGrammarParser