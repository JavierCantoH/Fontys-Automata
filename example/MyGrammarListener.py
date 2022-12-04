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


    # Enter a parse tree produced by MyGrammarParser#hello.
    def enterHello(self, ctx:MyGrammarParser.HelloContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#hello.
    def exitHello(self, ctx:MyGrammarParser.HelloContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#goodbye.
    def enterGoodbye(self, ctx:MyGrammarParser.GoodbyeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#goodbye.
    def exitGoodbye(self, ctx:MyGrammarParser.GoodbyeContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#name.
    def enterName(self, ctx:MyGrammarParser.NameContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#name.
    def exitName(self, ctx:MyGrammarParser.NameContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#age.
    def enterAge(self, ctx:MyGrammarParser.AgeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#age.
    def exitAge(self, ctx:MyGrammarParser.AgeContext):
        pass



del MyGrammarParser