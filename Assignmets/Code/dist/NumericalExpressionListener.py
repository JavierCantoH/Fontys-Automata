# Generated from NumericalExpression.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NumericalExpressionParser import NumericalExpressionParser
else:
    from NumericalExpressionParser import NumericalExpressionParser

# This class defines a complete listener for a parse tree produced by NumericalExpressionParser.
class NumericalExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by NumericalExpressionParser#prog.
    def enterProg(self, ctx:NumericalExpressionParser.ProgContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#prog.
    def exitProg(self, ctx:NumericalExpressionParser.ProgContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#print.
    def enterPrint(self, ctx:NumericalExpressionParser.PrintContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#print.
    def exitPrint(self, ctx:NumericalExpressionParser.PrintContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#assign.
    def enterAssign(self, ctx:NumericalExpressionParser.AssignContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#assign.
    def exitAssign(self, ctx:NumericalExpressionParser.AssignContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#blank.
    def enterBlank(self, ctx:NumericalExpressionParser.BlankContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#blank.
    def exitBlank(self, ctx:NumericalExpressionParser.BlankContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#parens.
    def enterParens(self, ctx:NumericalExpressionParser.ParensContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#parens.
    def exitParens(self, ctx:NumericalExpressionParser.ParensContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#id.
    def enterId(self, ctx:NumericalExpressionParser.IdContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#id.
    def exitId(self, ctx:NumericalExpressionParser.IdContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#operation.
    def enterOperation(self, ctx:NumericalExpressionParser.OperationContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#operation.
    def exitOperation(self, ctx:NumericalExpressionParser.OperationContext):
        pass


    # Enter a parse tree produced by NumericalExpressionParser#int.
    def enterInt(self, ctx:NumericalExpressionParser.IntContext):
        pass

    # Exit a parse tree produced by NumericalExpressionParser#int.
    def exitInt(self, ctx:NumericalExpressionParser.IntContext):
        pass



del NumericalExpressionParser