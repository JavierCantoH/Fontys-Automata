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
        4,1,8,33,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,18,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,26,8,1,10,1,12,
        1,29,9,1,1,2,1,2,1,2,0,1,2,3,0,2,4,0,2,1,0,2,3,2,0,1,1,4,4,33,0,
        6,1,0,0,0,2,17,1,0,0,0,4,30,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,
        1,0,0,0,9,10,6,1,-1,0,10,11,5,1,0,0,11,18,3,2,1,5,12,13,5,5,0,0,
        13,14,3,2,1,0,14,15,5,6,0,0,15,18,1,0,0,0,16,18,5,8,0,0,17,9,1,0,
        0,0,17,12,1,0,0,0,17,16,1,0,0,0,18,27,1,0,0,0,19,20,10,4,0,0,20,
        21,7,0,0,0,21,26,3,2,1,5,22,23,10,3,0,0,23,24,7,1,0,0,24,26,3,2,
        1,4,25,19,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,
        1,0,0,0,28,3,1,0,0,0,29,27,1,0,0,0,30,31,5,8,0,0,31,5,1,0,0,0,3,
        17,25,27
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'*'", "'/'", "'+'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "NUM" ]

    RULE_myStart = 0
    RULE_expr = 1
    RULE_num = 2

    ruleNames =  [ "myStart", "expr", "num" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WS=7
    NUM=8

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

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr(0)
            self.state = 7
            self.match(MyGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExprContext,i)


        def NUM(self):
            return self.getToken(MyGrammarParser.NUM, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 10
                self.match(MyGrammarParser.T__0)
                self.state = 11
                self.expr(5)
                pass
            elif token in [5]:
                self.state = 12
                self.match(MyGrammarParser.T__4)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(MyGrammarParser.T__5)
                pass
            elif token in [8]:
                self.state = 16
                self.match(MyGrammarParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 25
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 20
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 21
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 23
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 24
                        self.expr(4)
                        pass

             
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(MyGrammarParser.NUM, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)




    def num(self):

        localctx = MyGrammarParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MyGrammarParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




