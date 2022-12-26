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


    # Enter a parse tree produced by MyGrammarParser#check_sat.
    def enterCheck_sat(self, ctx:MyGrammarParser.Check_satContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#check_sat.
    def exitCheck_sat(self, ctx:MyGrammarParser.Check_satContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#get_model.
    def enterGet_model(self, ctx:MyGrammarParser.Get_modelContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#get_model.
    def exitGet_model(self, ctx:MyGrammarParser.Get_modelContext):
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