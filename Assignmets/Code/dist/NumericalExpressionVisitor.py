# Generated from NumericalExpression.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NumericalExpressionParser import NumericalExpressionParser
else:
    from NumericalExpressionParser import NumericalExpressionParser

# This class defines a complete generic visitor for a parse tree produced by NumericalExpressionParser.

class NumericalExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NumericalExpressionParser#prog.
    def visitProg(self, ctx:NumericalExpressionParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#print.
    def visitPrint(self, ctx:NumericalExpressionParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#assign.
    def visitAssign(self, ctx:NumericalExpressionParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#blank.
    def visitBlank(self, ctx:NumericalExpressionParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#parens.
    def visitParens(self, ctx:NumericalExpressionParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#id.
    def visitId(self, ctx:NumericalExpressionParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#operation.
    def visitOperation(self, ctx:NumericalExpressionParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NumericalExpressionParser#int.
    def visitInt(self, ctx:NumericalExpressionParser.IntContext):
        return self.visitChildren(ctx)



del NumericalExpressionParser