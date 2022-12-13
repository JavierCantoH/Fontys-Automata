# Generated from NumericalExpression.g4 by ANTLR 4.11.1
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
        4,1,11,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,3,
        0,14,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,30,8,3,1,3,1,3,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,1,4,1,4,1,
        4,0,1,6,5,0,2,4,6,8,0,1,1,0,5,8,42,0,13,1,0,0,0,2,15,1,0,0,0,4,19,
        1,0,0,0,6,29,1,0,0,0,8,40,1,0,0,0,10,14,3,2,1,0,11,14,3,4,2,0,12,
        14,3,6,3,0,13,10,1,0,0,0,13,11,1,0,0,0,13,12,1,0,0,0,14,1,1,0,0,
        0,15,16,5,9,0,0,16,17,5,1,0,0,17,18,3,6,3,0,18,3,1,0,0,0,19,20,5,
        2,0,0,20,21,5,9,0,0,21,5,1,0,0,0,22,23,6,3,-1,0,23,30,5,10,0,0,24,
        30,5,9,0,0,25,26,5,3,0,0,26,27,3,6,3,0,27,28,5,4,0,0,28,30,1,0,0,
        0,29,22,1,0,0,0,29,24,1,0,0,0,29,25,1,0,0,0,30,37,1,0,0,0,31,32,
        10,2,0,0,32,33,3,8,4,0,33,34,3,6,3,3,34,36,1,0,0,0,35,31,1,0,0,0,
        36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,7,1,0,0,0,39,37,1,0,
        0,0,40,41,7,0,0,0,41,9,1,0,0,0,3,13,29,37
    ]

class NumericalExpressionParser ( Parser ):

    grammarFileName = "NumericalExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'print'", "'('", "')'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VariableName", "Number", "WS" ]

    RULE_numericalExpression = 0
    RULE_variableAssignment = 1
    RULE_printStatement = 2
    RULE_mathematicalExpression = 3
    RULE_operator = 4

    ruleNames =  [ "numericalExpression", "variableAssignment", "printStatement", 
                   "mathematicalExpression", "operator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    VariableName=9
    Number=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NumericalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableAssignment(self):
            return self.getTypedRuleContext(NumericalExpressionParser.VariableAssignmentContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(NumericalExpressionParser.PrintStatementContext,0)


        def mathematicalExpression(self):
            return self.getTypedRuleContext(NumericalExpressionParser.MathematicalExpressionContext,0)


        def getRuleIndex(self):
            return NumericalExpressionParser.RULE_numericalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericalExpression" ):
                listener.enterNumericalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericalExpression" ):
                listener.exitNumericalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericalExpression" ):
                return visitor.visitNumericalExpression(self)
            else:
                return visitor.visitChildren(self)




    def numericalExpression(self):

        localctx = NumericalExpressionParser.NumericalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_numericalExpression)
        try:
            self.state = 13
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.variableAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.mathematicalExpression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VariableName(self):
            return self.getToken(NumericalExpressionParser.VariableName, 0)

        def mathematicalExpression(self):
            return self.getTypedRuleContext(NumericalExpressionParser.MathematicalExpressionContext,0)


        def getRuleIndex(self):
            return NumericalExpressionParser.RULE_variableAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableAssignment" ):
                listener.enterVariableAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableAssignment" ):
                listener.exitVariableAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAssignment" ):
                return visitor.visitVariableAssignment(self)
            else:
                return visitor.visitChildren(self)




    def variableAssignment(self):

        localctx = NumericalExpressionParser.VariableAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(NumericalExpressionParser.VariableName)
            self.state = 16
            self.match(NumericalExpressionParser.T__0)
            self.state = 17
            self.mathematicalExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VariableName(self):
            return self.getToken(NumericalExpressionParser.VariableName, 0)

        def getRuleIndex(self):
            return NumericalExpressionParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = NumericalExpressionParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(NumericalExpressionParser.T__1)
            self.state = 20
            self.match(NumericalExpressionParser.VariableName)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathematicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number(self):
            return self.getToken(NumericalExpressionParser.Number, 0)

        def VariableName(self):
            return self.getToken(NumericalExpressionParser.VariableName, 0)

        def mathematicalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumericalExpressionParser.MathematicalExpressionContext)
            else:
                return self.getTypedRuleContext(NumericalExpressionParser.MathematicalExpressionContext,i)


        def operator(self):
            return self.getTypedRuleContext(NumericalExpressionParser.OperatorContext,0)


        def getRuleIndex(self):
            return NumericalExpressionParser.RULE_mathematicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathematicalExpression" ):
                listener.enterMathematicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathematicalExpression" ):
                listener.exitMathematicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathematicalExpression" ):
                return visitor.visitMathematicalExpression(self)
            else:
                return visitor.visitChildren(self)



    def mathematicalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = NumericalExpressionParser.MathematicalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_mathematicalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 23
                self.match(NumericalExpressionParser.Number)
                pass
            elif token in [9]:
                self.state = 24
                self.match(NumericalExpressionParser.VariableName)
                pass
            elif token in [3]:
                self.state = 25
                self.match(NumericalExpressionParser.T__2)
                self.state = 26
                self.mathematicalExpression(0)
                self.state = 27
                self.match(NumericalExpressionParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = NumericalExpressionParser.MathematicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mathematicalExpression)
                    self.state = 31
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 32
                    self.operator()
                    self.state = 33
                    self.mathematicalExpression(3) 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NumericalExpressionParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = NumericalExpressionParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.mathematicalExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def mathematicalExpression_sempred(self, localctx:MathematicalExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




