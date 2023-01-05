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


    # Enter a parse tree produced by MyGrammarParser#statement.
    def enterStatement(self, ctx:MyGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#statement.
    def exitStatement(self, ctx:MyGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#declaration.
    def enterDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#declaration.
    def exitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#checksat.
    def enterChecksat(self, ctx:MyGrammarParser.ChecksatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#checksat.
    def exitChecksat(self, ctx:MyGrammarParser.ChecksatContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#getmodel.
    def enterGetmodel(self, ctx:MyGrammarParser.GetmodelContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#getmodel.
    def exitGetmodel(self, ctx:MyGrammarParser.GetmodelContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#assertion.
    def enterAssertion(self, ctx:MyGrammarParser.AssertionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assertion.
    def exitAssertion(self, ctx:MyGrammarParser.AssertionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#constraint.
    def enterConstraint(self, ctx:MyGrammarParser.ConstraintContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#constraint.
    def exitConstraint(self, ctx:MyGrammarParser.ConstraintContext):
        pass



del MyGrammarParser