# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#AtomExpr.
    def enterAtomExpr(self, ctx:MyGrammarParser.AtomExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#AtomExpr.
    def exitAtomExpr(self, ctx:MyGrammarParser.AtomExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#ParenExpr.
    def enterParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#ParenExpr.
    def exitParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#OpExpr.
    def enterOpExpr(self, ctx:MyGrammarParser.OpExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#OpExpr.
    def exitOpExpr(self, ctx:MyGrammarParser.OpExprContext):
        pass



del MyGrammarParser