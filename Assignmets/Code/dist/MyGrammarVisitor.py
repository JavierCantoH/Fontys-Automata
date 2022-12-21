# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#prog.
    def visitProg(self, ctx:MyGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MyGrammarParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#returnFunc.
    def visitReturnFunc(self, ctx:MyGrammarParser.ReturnFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#callingFunc.
    def visitCallingFunc(self, ctx:MyGrammarParser.CallingFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#printLine.
    def visitPrintLine(self, ctx:MyGrammarParser.PrintLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assign.
    def visitAssign(self, ctx:MyGrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assignExpr.
    def visitAssignExpr(self, ctx:MyGrammarParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#blank.
    def visitBlank(self, ctx:MyGrammarParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#printExpr.
    def visitPrintExpr(self, ctx:MyGrammarParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#ifExpr.
    def visitIfExpr(self, ctx:MyGrammarParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#loopExpr.
    def visitLoopExpr(self, ctx:MyGrammarParser.LoopExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#number.
    def visitNumber(self, ctx:MyGrammarParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#parens.
    def visitParens(self, ctx:MyGrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#id.
    def visitId(self, ctx:MyGrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#text.
    def visitText(self, ctx:MyGrammarParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#operation.
    def visitOperation(self, ctx:MyGrammarParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#exprFuncCall.
    def visitExprFuncCall(self, ctx:MyGrammarParser.ExprFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#functionDecl.
    def visitFunctionDecl(self, ctx:MyGrammarParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#block.
    def visitBlock(self, ctx:MyGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#formalParameters.
    def visitFormalParameters(self, ctx:MyGrammarParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#formalParameter.
    def visitFormalParameter(self, ctx:MyGrammarParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#exprList.
    def visitExprList(self, ctx:MyGrammarParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#print.
    def visitPrint(self, ctx:MyGrammarParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#loop.
    def visitLoop(self, ctx:MyGrammarParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#ifStat.
    def visitIfStat(self, ctx:MyGrammarParser.IfStatContext):
        return self.visitChildren(ctx)



del MyGrammarParser