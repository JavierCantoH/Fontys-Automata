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
        4,1,11,39,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,4,0,9,8,0,11,0,12,0,10,
        1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,26,8,2,1,
        2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,0,1,4,3,0,
        2,4,0,2,1,0,2,3,1,0,4,5,41,0,8,1,0,0,0,2,14,1,0,0,0,4,25,1,0,0,0,
        6,9,3,2,1,0,7,9,3,4,2,0,8,6,1,0,0,0,8,7,1,0,0,0,9,10,1,0,0,0,10,
        8,1,0,0,0,10,11,1,0,0,0,11,12,1,0,0,0,12,13,5,0,0,1,13,1,1,0,0,0,
        14,15,5,9,0,0,15,16,5,1,0,0,16,17,5,8,0,0,17,3,1,0,0,0,18,19,6,2,
        -1,0,19,26,5,8,0,0,20,26,5,9,0,0,21,22,5,6,0,0,22,23,3,4,2,0,23,
        24,5,7,0,0,24,26,1,0,0,0,25,18,1,0,0,0,25,20,1,0,0,0,25,21,1,0,0,
        0,26,35,1,0,0,0,27,28,10,5,0,0,28,29,7,0,0,0,29,34,3,4,2,6,30,31,
        10,4,0,0,31,32,7,1,0,0,32,34,3,4,2,5,33,27,1,0,0,0,33,30,1,0,0,0,
        34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,35,1,0,
        0,0,5,8,10,25,33,35
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "'INT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "ID", "WS", "INT_TYPE" ]

    RULE_prog = 0
    RULE_decl = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "decl", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUM=8
    ID=9
    WS=10
    INT_TYPE=11

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


        def getRuleIndex(self):
            return MyGrammarParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)
        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.DeclContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.DeclContext,i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = MyGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            localctx = MyGrammarParser.ProgramContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 8 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 6
                    self.decl()
                    pass

                elif la_ == 2:
                    self.state = 7
                    self.expr(0)
                    pass


                self.state = 10 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 832) != 0):
                    break

            self.state = 12
            self.match(MyGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclarationContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.DeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)
        def NUM(self):
            return self.getToken(MyGrammarParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def decl(self):

        localctx = MyGrammarParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            localctx = MyGrammarParser.DeclarationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(MyGrammarParser.ID)
            self.state = 15
            self.match(MyGrammarParser.T__0)
            self.state = 16
            self.match(MyGrammarParser.NUM)
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


        def getRuleIndex(self):
            return MyGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.id_ = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.num = None # Token
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(MyGrammarParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class OperationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperationExpr" ):
                listener.enterOperationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperationExpr" ):
                listener.exitOperationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperationExpr" ):
                return visitor.visitOperationExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentExpr" ):
                listener.enterParentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentExpr" ):
                listener.exitParentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentExpr" ):
                return visitor.visitParentExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = MyGrammarParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                localctx.num = self.match(MyGrammarParser.NUM)
                pass
            elif token in [9]:
                localctx = MyGrammarParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                localctx.id_ = self.match(MyGrammarParser.ID)
                pass
            elif token in [6]:
                localctx = MyGrammarParser.ParentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(MyGrammarParser.T__5)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(MyGrammarParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OperationExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 28
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OperationExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




