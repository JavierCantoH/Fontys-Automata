# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#myStart.
    def enterMyStart(self, ctx:MyGrammarParser.MyStartContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#myStart.
    def exitMyStart(self, ctx:MyGrammarParser.MyStartContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx:MyGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx:MyGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#num.
    def enterNum(self, ctx:MyGrammarParser.NumContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#num.
    def exitNum(self, ctx:MyGrammarParser.NumContext):
        pass



del MyGrammarParser