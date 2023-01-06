# Generated from MyGrammar2.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammar2Parser import MyGrammar2Parser
else:
    from MyGrammar2Parser import MyGrammar2Parser

# This class defines a complete listener for a parse tree produced by MyGrammar2Parser.
class MyGrammar2Listener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammar2Parser#program.
    def enterProgram(self, ctx:MyGrammar2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#program.
    def exitProgram(self, ctx:MyGrammar2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#command.
    def enterCommand(self, ctx:MyGrammar2Parser.CommandContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#command.
    def exitCommand(self, ctx:MyGrammar2Parser.CommandContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#declare_fun.
    def enterDeclare_fun(self, ctx:MyGrammar2Parser.Declare_funContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#declare_fun.
    def exitDeclare_fun(self, ctx:MyGrammar2Parser.Declare_funContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#assert_cmd.
    def enterAssert_cmd(self, ctx:MyGrammar2Parser.Assert_cmdContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#assert_cmd.
    def exitAssert_cmd(self, ctx:MyGrammar2Parser.Assert_cmdContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#distinct_formula.
    def enterDistinct_formula(self, ctx:MyGrammar2Parser.Distinct_formulaContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#distinct_formula.
    def exitDistinct_formula(self, ctx:MyGrammar2Parser.Distinct_formulaContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#values.
    def enterValues(self, ctx:MyGrammar2Parser.ValuesContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#values.
    def exitValues(self, ctx:MyGrammar2Parser.ValuesContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#formula.
    def enterFormula(self, ctx:MyGrammar2Parser.FormulaContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#formula.
    def exitFormula(self, ctx:MyGrammar2Parser.FormulaContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#comparator.
    def enterComparator(self, ctx:MyGrammar2Parser.ComparatorContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#comparator.
    def exitComparator(self, ctx:MyGrammar2Parser.ComparatorContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#comp.
    def enterComp(self, ctx:MyGrammar2Parser.CompContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#comp.
    def exitComp(self, ctx:MyGrammar2Parser.CompContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#check_sat.
    def enterCheck_sat(self, ctx:MyGrammar2Parser.Check_satContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#check_sat.
    def exitCheck_sat(self, ctx:MyGrammar2Parser.Check_satContext):
        pass


    # Enter a parse tree produced by MyGrammar2Parser#get_model.
    def enterGet_model(self, ctx:MyGrammar2Parser.Get_modelContext):
        pass

    # Exit a parse tree produced by MyGrammar2Parser#get_model.
    def exitGet_model(self, ctx:MyGrammar2Parser.Get_modelContext):
        pass



del MyGrammar2Parser