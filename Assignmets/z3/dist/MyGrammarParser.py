# Generated from MyGrammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,4,6,51,8,6,11,6,12,6,52,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,93,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,13,14,99,
        0,17,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,34,1,0,0,0,8,38,1,0,0,0,
        10,42,1,0,0,0,12,92,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,
        0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,17,1,0,0,0,20,
        25,3,4,2,0,21,25,3,6,3,0,22,25,3,8,4,0,23,25,3,10,5,0,24,20,1,0,
        0,0,24,21,1,0,0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,3,1,0,0,0,26,27,
        5,9,0,0,27,28,5,11,0,0,28,29,5,13,0,0,29,30,5,9,0,0,30,31,5,10,0,
        0,31,32,5,12,0,0,32,33,5,10,0,0,33,5,1,0,0,0,34,35,5,9,0,0,35,36,
        5,17,0,0,36,37,5,10,0,0,37,7,1,0,0,0,38,39,5,9,0,0,39,40,5,18,0,
        0,40,41,5,10,0,0,41,9,1,0,0,0,42,43,5,9,0,0,43,44,5,15,0,0,44,45,
        3,12,6,0,45,46,5,10,0,0,46,11,1,0,0,0,47,48,5,9,0,0,48,50,5,16,0,
        0,49,51,5,13,0,0,50,49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,
        1,0,0,0,53,54,1,0,0,0,54,93,5,10,0,0,55,56,5,9,0,0,56,57,5,7,0,0,
        57,58,3,12,6,0,58,59,3,12,6,0,59,60,5,10,0,0,60,93,1,0,0,0,61,62,
        5,9,0,0,62,63,5,8,0,0,63,64,3,12,6,0,64,65,3,12,6,0,65,66,5,10,0,
        0,66,93,1,0,0,0,67,68,5,9,0,0,68,69,5,2,0,0,69,70,7,0,0,0,70,71,
        7,0,0,0,71,93,5,10,0,0,72,73,5,9,0,0,73,74,5,3,0,0,74,75,7,0,0,0,
        75,76,7,0,0,0,76,93,5,10,0,0,77,78,5,9,0,0,78,79,5,4,0,0,79,80,7,
        0,0,0,80,81,7,0,0,0,81,93,5,10,0,0,82,83,5,9,0,0,83,84,5,5,0,0,84,
        85,7,0,0,0,85,86,7,0,0,0,86,93,5,10,0,0,87,88,5,9,0,0,88,89,5,6,
        0,0,89,90,7,0,0,0,90,91,7,0,0,0,91,93,5,10,0,0,92,47,1,0,0,0,92,
        55,1,0,0,0,92,61,1,0,0,0,92,67,1,0,0,0,92,72,1,0,0,0,92,77,1,0,0,
        0,92,82,1,0,0,0,92,87,1,0,0,0,93,13,1,0,0,0,4,17,24,52,92
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'>'", "'<'", "'>='", "'<='", "'='", 
                     "'and'", "'or'", "'('", "')'", "'declare-fun'", "'Int'", 
                     "<INVALID>", "<INVALID>", "'assert'", "'distinct'", 
                     "'check-sat'", "'get-model'" ]

    symbolicNames = [ "<INVALID>", "SEMICOLON", "GREATER", "LESS", "GREATER_EQUAL", 
                      "LESS_EQUAL", "BOOLEAN_EQUAL", "AND", "OR", "OPENPARENS", 
                      "CLOSINGPARENS", "DECLAREFUN", "INT", "ID", "NUMBER", 
                      "ASSERTWORD", "DISTINCT", "CHECKSATWORD", "GETMODELWORD", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_checksat = 3
    RULE_getmodel = 4
    RULE_assertion = 5
    RULE_constraint = 6

    ruleNames =  [ "prog", "statement", "declaration", "checksat", "getmodel", 
                   "assertion", "constraint" ]

    EOF = Token.EOF
    SEMICOLON=1
    GREATER=2
    LESS=3
    GREATER_EQUAL=4
    LESS_EQUAL=5
    BOOLEAN_EQUAL=6
    AND=7
    OR=8
    OPENPARENS=9
    CLOSINGPARENS=10
    DECLAREFUN=11
    INT=12
    ID=13
    NUMBER=14
    ASSERTWORD=15
    DISTINCT=16
    CHECKSATWORD=17
    GETMODELWORD=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MyGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MyGrammarParser.DeclarationContext,0)


        def checksat(self):
            return self.getTypedRuleContext(MyGrammarParser.ChecksatContext,0)


        def getmodel(self):
            return self.getTypedRuleContext(MyGrammarParser.GetmodelContext,0)


        def assertion(self):
            return self.getTypedRuleContext(MyGrammarParser.AssertionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.checksat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.getmodel()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.assertion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENS(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.OPENPARENS)
            else:
                return self.getToken(MyGrammarParser.OPENPARENS, i)

        def DECLAREFUN(self):
            return self.getToken(MyGrammarParser.DECLAREFUN, 0)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def CLOSINGPARENS(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.CLOSINGPARENS)
            else:
                return self.getToken(MyGrammarParser.CLOSINGPARENS, i)

        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = MyGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 27
            self.match(MyGrammarParser.DECLAREFUN)
            self.state = 28
            self.match(MyGrammarParser.ID)
            self.state = 29
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 30
            self.match(MyGrammarParser.CLOSINGPARENS)
            self.state = 31
            self.match(MyGrammarParser.INT)
            self.state = 32
            self.match(MyGrammarParser.CLOSINGPARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChecksatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)

        def CHECKSATWORD(self):
            return self.getToken(MyGrammarParser.CHECKSATWORD, 0)

        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_checksat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChecksat" ):
                listener.enterChecksat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChecksat" ):
                listener.exitChecksat(self)




    def checksat(self):

        localctx = MyGrammarParser.ChecksatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_checksat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 35
            self.match(MyGrammarParser.CHECKSATWORD)
            self.state = 36
            self.match(MyGrammarParser.CLOSINGPARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetmodelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)

        def GETMODELWORD(self):
            return self.getToken(MyGrammarParser.GETMODELWORD, 0)

        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_getmodel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetmodel" ):
                listener.enterGetmodel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetmodel" ):
                listener.exitGetmodel(self)




    def getmodel(self):

        localctx = MyGrammarParser.GetmodelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_getmodel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 39
            self.match(MyGrammarParser.GETMODELWORD)
            self.state = 40
            self.match(MyGrammarParser.CLOSINGPARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)

        def ASSERTWORD(self):
            return self.getToken(MyGrammarParser.ASSERTWORD, 0)

        def constraint(self):
            return self.getTypedRuleContext(MyGrammarParser.ConstraintContext,0)


        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_assertion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertion" ):
                listener.enterAssertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertion" ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = MyGrammarParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 43
            self.match(MyGrammarParser.ASSERTWORD)
            self.state = 44
            self.constraint()
            self.state = 45
            self.match(MyGrammarParser.CLOSINGPARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)

        def DISTINCT(self):
            return self.getToken(MyGrammarParser.DISTINCT, 0)

        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.ID)
            else:
                return self.getToken(MyGrammarParser.ID, i)

        def AND(self):
            return self.getToken(MyGrammarParser.AND, 0)

        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ConstraintContext,i)


        def OR(self):
            return self.getToken(MyGrammarParser.OR, 0)

        def GREATER(self):
            return self.getToken(MyGrammarParser.GREATER, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.NUMBER)
            else:
                return self.getToken(MyGrammarParser.NUMBER, i)

        def LESS(self):
            return self.getToken(MyGrammarParser.LESS, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MyGrammarParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(MyGrammarParser.LESS_EQUAL, 0)

        def BOOLEAN_EQUAL(self):
            return self.getToken(MyGrammarParser.BOOLEAN_EQUAL, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint" ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint" ):
                listener.exitConstraint(self)




    def constraint(self):

        localctx = MyGrammarParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constraint)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 48
                self.match(MyGrammarParser.DISTINCT)
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 49
                    self.match(MyGrammarParser.ID)
                    self.state = 52 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13):
                        break

                self.state = 54
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 56
                self.match(MyGrammarParser.AND)
                self.state = 57
                self.constraint()
                self.state = 58
                self.constraint()
                self.state = 59
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 62
                self.match(MyGrammarParser.OR)
                self.state = 63
                self.constraint()
                self.state = 64
                self.constraint()
                self.state = 65
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 68
                self.match(MyGrammarParser.GREATER)
                self.state = 69
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 71
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 73
                self.match(MyGrammarParser.LESS)
                self.state = 74
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 76
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 78
                self.match(MyGrammarParser.GREATER_EQUAL)
                self.state = 79
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 80
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 81
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 83
                self.match(MyGrammarParser.LESS_EQUAL)
                self.state = 84
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 85
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 86
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 87
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 88
                self.match(MyGrammarParser.BOOLEAN_EQUAL)
                self.state = 89
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 90
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 91
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





