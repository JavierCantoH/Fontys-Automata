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
        4,1,5,29,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,4,0,13,
        8,0,11,0,12,0,14,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        1,4,0,0,5,0,2,4,6,8,0,0,25,0,12,1,0,0,0,2,18,1,0,0,0,4,22,1,0,0,
        0,6,24,1,0,0,0,8,26,1,0,0,0,10,13,3,2,1,0,11,13,3,4,2,0,12,10,1,
        0,0,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,
        16,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,5,2,0,0,19,20,3,6,3,
        0,20,21,3,8,4,0,21,3,1,0,0,0,22,23,5,1,0,0,23,5,1,0,0,0,24,25,5,
        4,0,0,25,7,1,0,0,0,26,27,5,3,0,0,27,9,1,0,0,0,2,12,14
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Bye'", "'Hello'" ]

    symbolicNames = [ "<INVALID>", "GOODBYE", "HELLO", "NUMBER", "ID", "WS" ]

    RULE_myStart = 0
    RULE_hello = 1
    RULE_goodbye = 2
    RULE_name = 3
    RULE_age = 4

    ruleNames =  [ "myStart", "hello", "goodbye", "name", "age" ]

    EOF = Token.EOF
    GOODBYE=1
    HELLO=2
    NUMBER=3
    ID=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MyStartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)

        def hello(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.HelloContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.HelloContext,i)


        def goodbye(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.GoodbyeContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.GoodbyeContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_myStart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMyStart" ):
                listener.enterMyStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMyStart" ):
                listener.exitMyStart(self)




    def myStart(self):

        localctx = MyGrammarParser.MyStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_myStart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 10
                    self.hello()
                    pass
                elif token in [1]:
                    self.state = 11
                    self.goodbye()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 16
            self.match(MyGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HELLO(self):
            return self.getToken(MyGrammarParser.HELLO, 0)

        def name(self):
            return self.getTypedRuleContext(MyGrammarParser.NameContext,0)


        def age(self):
            return self.getTypedRuleContext(MyGrammarParser.AgeContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_hello

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHello" ):
                listener.enterHello(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHello" ):
                listener.exitHello(self)




    def hello(self):

        localctx = MyGrammarParser.HelloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hello)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(MyGrammarParser.HELLO)
            self.state = 19
            self.name()
            self.state = 20
            self.age()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoodbyeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOODBYE(self):
            return self.getToken(MyGrammarParser.GOODBYE, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_goodbye

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoodbye" ):
                listener.enterGoodbye(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoodbye" ):
                listener.exitGoodbye(self)




    def goodbye(self):

        localctx = MyGrammarParser.GoodbyeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_goodbye)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(MyGrammarParser.GOODBYE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = MyGrammarParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MyGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MyGrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_age

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAge" ):
                listener.enterAge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAge" ):
                listener.exitAge(self)




    def age(self):

        localctx = MyGrammarParser.AgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_age)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(MyGrammarParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





