# Generated from MyGrammar2.g4 by ANTLR 4.11.1
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
        4,1,20,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,51,8,4,10,4,12,4,54,9,4,1,4,1,
        4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,74,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,3,1,0,18,19,1,0,8,12,1,
        0,13,14,84,0,23,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,40,1,0,0,0,8,
        45,1,0,0,0,10,57,1,0,0,0,12,73,1,0,0,0,14,75,1,0,0,0,16,77,1,0,0,
        0,18,79,1,0,0,0,20,83,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,
        1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,0,0,27,32,3,4,2,0,28,
        32,3,6,3,0,29,32,3,18,9,0,30,32,3,20,10,0,31,27,1,0,0,0,31,28,1,
        0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,1,0,0,34,
        35,5,2,0,0,35,36,5,18,0,0,36,37,5,3,0,0,37,38,5,4,0,0,38,39,5,5,
        0,0,39,5,1,0,0,0,40,41,5,1,0,0,41,42,5,6,0,0,42,43,3,12,6,0,43,44,
        5,5,0,0,44,7,1,0,0,0,45,46,5,1,0,0,46,47,5,7,0,0,47,48,3,10,5,0,
        48,52,3,10,5,0,49,51,3,10,5,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,5,5,0,0,
        56,9,1,0,0,0,57,58,7,0,0,0,58,11,1,0,0,0,59,74,3,8,4,0,60,61,5,1,
        0,0,61,62,3,16,8,0,62,63,3,12,6,0,63,64,3,12,6,0,64,65,5,5,0,0,65,
        74,1,0,0,0,66,67,5,1,0,0,67,68,3,14,7,0,68,69,3,10,5,0,69,70,3,10,
        5,0,70,71,5,5,0,0,71,74,1,0,0,0,72,74,3,10,5,0,73,59,1,0,0,0,73,
        60,1,0,0,0,73,66,1,0,0,0,73,72,1,0,0,0,74,13,1,0,0,0,75,76,7,1,0,
        0,76,15,1,0,0,0,77,78,7,2,0,0,78,17,1,0,0,0,79,80,5,1,0,0,80,81,
        5,15,0,0,81,82,5,5,0,0,82,19,1,0,0,0,83,84,5,1,0,0,84,85,5,16,0,
        0,85,86,5,5,0,0,86,21,1,0,0,0,4,25,31,52,73
    ]

class MyGrammar2Parser ( Parser ):

    grammarFileName = "MyGrammar2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "'declare-fun'", "'()'", "'Int'", 
                     "')'", "'assert'", "'distinct'", "'>='", "'<='", "'<'", 
                     "'>'", "'='", "'and'", "'or'", "'check-sat'", "'get-model'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_command = 1
    RULE_declare_fun = 2
    RULE_assert_cmd = 3
    RULE_distinct_formula = 4
    RULE_values = 5
    RULE_formula = 6
    RULE_comparator = 7
    RULE_comp = 8
    RULE_check_sat = 9
    RULE_get_model = 10

    ruleNames =  [ "program", "command", "declare_fun", "assert_cmd", "distinct_formula", 
                   "values", "formula", "comparator", "comp", "check_sat", 
                   "get_model" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    COMMENT=17
    ID=18
    NUMBER=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.CommandContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.CommandContext,i)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyGrammar2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.command()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_fun(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Declare_funContext,0)


        def assert_cmd(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Assert_cmdContext,0)


        def check_sat(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Check_satContext,0)


        def get_model(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Get_modelContext,0)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = MyGrammar2Parser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.declare_fun()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.assert_cmd()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.check_sat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.get_model()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_funContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammar2Parser.ID, 0)

        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_declare_fun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_fun" ):
                listener.enterDeclare_fun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_fun" ):
                listener.exitDeclare_fun(self)




    def declare_fun(self):

        localctx = MyGrammar2Parser.Declare_funContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare_fun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MyGrammar2Parser.T__0)
            self.state = 34
            self.match(MyGrammar2Parser.T__1)
            self.state = 35
            self.match(MyGrammar2Parser.ID)
            self.state = 36
            self.match(MyGrammar2Parser.T__2)
            self.state = 37
            self.match(MyGrammar2Parser.T__3)
            self.state = 38
            self.match(MyGrammar2Parser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assert_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(MyGrammar2Parser.FormulaContext,0)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_assert_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssert_cmd" ):
                listener.enterAssert_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssert_cmd" ):
                listener.exitAssert_cmd(self)




    def assert_cmd(self):

        localctx = MyGrammar2Parser.Assert_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assert_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MyGrammar2Parser.T__0)
            self.state = 41
            self.match(MyGrammar2Parser.T__5)
            self.state = 42
            self.formula()
            self.state = 43
            self.match(MyGrammar2Parser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distinct_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.ValuesContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.ValuesContext,i)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_distinct_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistinct_formula" ):
                listener.enterDistinct_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistinct_formula" ):
                listener.exitDistinct_formula(self)




    def distinct_formula(self):

        localctx = MyGrammar2Parser.Distinct_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_distinct_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MyGrammar2Parser.T__0)
            self.state = 46
            self.match(MyGrammar2Parser.T__6)
            self.state = 47
            self.values()
            self.state = 48
            self.values()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 49
                self.values()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(MyGrammar2Parser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammar2Parser.ID, 0)

        def NUMBER(self):
            return self.getToken(MyGrammar2Parser.NUMBER, 0)

        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = MyGrammar2Parser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distinct_formula(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Distinct_formulaContext,0)


        def comp(self):
            return self.getTypedRuleContext(MyGrammar2Parser.CompContext,0)


        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.FormulaContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.FormulaContext,i)


        def comparator(self):
            return self.getTypedRuleContext(MyGrammar2Parser.ComparatorContext,0)


        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.ValuesContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.ValuesContext,i)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)




    def formula(self):

        localctx = MyGrammar2Parser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formula)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.distinct_formula()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(MyGrammar2Parser.T__0)
                self.state = 61
                self.comp()
                self.state = 62
                self.formula()
                self.state = 63
                self.formula()
                self.state = 64
                self.match(MyGrammar2Parser.T__4)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.match(MyGrammar2Parser.T__0)
                self.state = 67
                self.comparator()
                self.state = 68
                self.values()
                self.state = 69
                self.values()
                self.state = 70
                self.match(MyGrammar2Parser.T__4)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.values()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = MyGrammar2Parser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = MyGrammar2Parser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_check_sat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheck_sat" ):
                listener.enterCheck_sat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheck_sat" ):
                listener.exitCheck_sat(self)




    def check_sat(self):

        localctx = MyGrammar2Parser.Check_satContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_check_sat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MyGrammar2Parser.T__0)
            self.state = 80
            self.match(MyGrammar2Parser.T__14)
            self.state = 81
            self.match(MyGrammar2Parser.T__4)
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


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_get_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_model" ):
                listener.enterGet_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_model" ):
                listener.exitGet_model(self)




    def get_model(self):

        localctx = MyGrammar2Parser.Get_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_get_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MyGrammar2Parser.T__0)
            self.state = 84
            self.match(MyGrammar2Parser.T__15)
            self.state = 85
            self.match(MyGrammar2Parser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





