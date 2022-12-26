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
        4,1,19,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,4,6,50,8,6,11,6,12,6,51,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,92,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,13,14,98,0,
        15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,33,1,0,0,0,8,37,1,0,0,0,10,
        41,1,0,0,0,12,91,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,
        0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,24,3,4,2,0,20,24,3,
        6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,1,0,0,0,23,20,1,0,0,0,23,
        21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,9,0,0,26,27,5,11,0,
        0,27,28,5,13,0,0,28,29,5,9,0,0,29,30,5,10,0,0,30,31,5,12,0,0,31,
        32,5,10,0,0,32,5,1,0,0,0,33,34,5,9,0,0,34,35,5,17,0,0,35,36,5,10,
        0,0,36,7,1,0,0,0,37,38,5,9,0,0,38,39,5,18,0,0,39,40,5,10,0,0,40,
        9,1,0,0,0,41,42,5,9,0,0,42,43,5,15,0,0,43,44,3,12,6,0,44,45,5,10,
        0,0,45,11,1,0,0,0,46,47,5,9,0,0,47,49,5,16,0,0,48,50,5,13,0,0,49,
        48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,
        0,53,92,5,10,0,0,54,55,5,9,0,0,55,56,5,7,0,0,56,57,3,12,6,0,57,58,
        3,12,6,0,58,59,5,10,0,0,59,92,1,0,0,0,60,61,5,9,0,0,61,62,5,8,0,
        0,62,63,3,12,6,0,63,64,3,12,6,0,64,65,5,10,0,0,65,92,1,0,0,0,66,
        67,5,9,0,0,67,68,5,2,0,0,68,69,7,0,0,0,69,70,7,0,0,0,70,92,5,10,
        0,0,71,72,5,9,0,0,72,73,5,3,0,0,73,74,7,0,0,0,74,75,7,0,0,0,75,92,
        5,10,0,0,76,77,5,9,0,0,77,78,5,4,0,0,78,79,7,0,0,0,79,80,7,0,0,0,
        80,92,5,10,0,0,81,82,5,9,0,0,82,83,5,5,0,0,83,84,7,0,0,0,84,85,7,
        0,0,0,85,92,5,10,0,0,86,87,5,9,0,0,87,88,5,6,0,0,88,89,7,0,0,0,89,
        90,7,0,0,0,90,92,5,10,0,0,91,46,1,0,0,0,91,54,1,0,0,0,91,60,1,0,
        0,0,91,66,1,0,0,0,91,71,1,0,0,0,91,76,1,0,0,0,91,81,1,0,0,0,91,86,
        1,0,0,0,92,13,1,0,0,0,4,17,23,51,91
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
                      "ASSERT", "DISTINCT", "CHECKSAT", "GETMODEL", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_check_sat = 3
    RULE_get_model = 4
    RULE_assertion = 5
    RULE_constraint = 6

    ruleNames =  [ "prog", "statement", "declaration", "check_sat", "get_model", 
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
    ASSERT=15
    DISTINCT=16
    CHECKSAT=17
    GETMODEL=18
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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

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


        def check_sat(self):
            return self.getTypedRuleContext(MyGrammarParser.Check_satContext,0)


        def get_model(self):
            return self.getTypedRuleContext(MyGrammarParser.Get_modelContext,0)


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
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.check_sat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.get_model()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
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
            self.state = 25
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 26
            self.match(MyGrammarParser.DECLAREFUN)
            self.state = 27
            self.match(MyGrammarParser.ID)
            self.state = 28
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 29
            self.match(MyGrammarParser.CLOSINGPARENS)
            self.state = 30
            self.match(MyGrammarParser.INT)
            self.state = 31
            self.match(MyGrammarParser.CLOSINGPARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Check_satContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)

        def CHECKSAT(self):
            return self.getToken(MyGrammarParser.CHECKSAT, 0)

        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_check_sat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheck_sat" ):
                listener.enterCheck_sat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheck_sat" ):
                listener.exitCheck_sat(self)




    def check_sat(self):

        localctx = MyGrammarParser.Check_satContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_check_sat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 34
            self.match(MyGrammarParser.CHECKSAT)
            self.state = 35
            self.match(MyGrammarParser.CLOSINGPARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Get_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)

        def GETMODEL(self):
            return self.getToken(MyGrammarParser.GETMODEL, 0)

        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_get_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_model" ):
                listener.enterGet_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_model" ):
                listener.exitGet_model(self)




    def get_model(self):

        localctx = MyGrammarParser.Get_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_get_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 38
            self.match(MyGrammarParser.GETMODEL)
            self.state = 39
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

        def ASSERT(self):
            return self.getToken(MyGrammarParser.ASSERT, 0)

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
            self.state = 41
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 42
            self.match(MyGrammarParser.ASSERT)
            self.state = 43
            self.constraint()
            self.state = 44
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 47
                self.match(MyGrammarParser.DISTINCT)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 48
                    self.match(MyGrammarParser.ID)
                    self.state = 51 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13):
                        break

                self.state = 53
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 55
                self.match(MyGrammarParser.AND)
                self.state = 56
                self.constraint()
                self.state = 57
                self.constraint()
                self.state = 58
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 61
                self.match(MyGrammarParser.OR)
                self.state = 62
                self.constraint()
                self.state = 63
                self.constraint()
                self.state = 64
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 67
                self.match(MyGrammarParser.GREATER)
                self.state = 68
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 72
                self.match(MyGrammarParser.LESS)
                self.state = 73
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 74
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 77
                self.match(MyGrammarParser.GREATER_EQUAL)
                self.state = 78
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 79
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 80
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 82
                self.match(MyGrammarParser.LESS_EQUAL)
                self.state = 83
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 84
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 85
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 87
                self.match(MyGrammarParser.BOOLEAN_EQUAL)
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 89
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 90
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





