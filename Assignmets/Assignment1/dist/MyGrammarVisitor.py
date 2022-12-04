# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#AtomExpr.
    def visitAtomExpr(self, ctx:MyGrammarParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#ParenExpr.
    def visitParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#OpExpr.
    def visitOpExpr(self, ctx:MyGrammarParser.OpExprContext):
        return self.visitChildren(ctx)



del MyGrammarParser