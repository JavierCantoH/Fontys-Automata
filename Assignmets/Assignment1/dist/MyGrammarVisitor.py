# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#Program.
    def visitProgram(self, ctx:MyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#Declaration.
    def visitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#Variable.
    def visitVariable(self, ctx:MyGrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#Number.
    def visitNumber(self, ctx:MyGrammarParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#OperationExpr.
    def visitOperationExpr(self, ctx:MyGrammarParser.OperationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#ParentExpr.
    def visitParentExpr(self, ctx:MyGrammarParser.ParentExprContext):
        return self.visitChildren(ctx)



del MyGrammarParser