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
        4,1,21,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,70,8,5,1,
        5,1,5,1,5,0,1,4,6,0,2,4,6,8,10,0,3,1,0,15,16,1,0,17,18,1,0,4,5,80,
        0,13,1,0,0,0,2,29,1,0,0,0,4,39,1,0,0,0,6,55,1,0,0,0,8,58,1,0,0,0,
        10,63,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,
        0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,13,0,0,19,
        30,1,0,0,0,20,21,5,14,0,0,21,22,5,11,0,0,22,23,3,4,2,0,23,24,5,13,
        0,0,24,30,1,0,0,0,25,30,5,13,0,0,26,30,3,6,3,0,27,30,3,10,5,0,28,
        30,3,8,4,0,29,17,1,0,0,0,29,20,1,0,0,0,29,25,1,0,0,0,29,26,1,0,0,
        0,29,27,1,0,0,0,29,28,1,0,0,0,30,3,1,0,0,0,31,32,6,2,-1,0,32,40,
        5,12,0,0,33,40,5,14,0,0,34,35,5,19,0,0,35,36,3,4,2,0,36,37,5,20,
        0,0,37,40,1,0,0,0,38,40,5,1,0,0,39,31,1,0,0,0,39,33,1,0,0,0,39,34,
        1,0,0,0,39,38,1,0,0,0,40,52,1,0,0,0,41,42,10,7,0,0,42,43,7,0,0,0,
        43,51,3,4,2,8,44,45,10,6,0,0,45,46,7,1,0,0,46,51,3,4,2,7,47,48,10,
        5,0,0,48,49,7,2,0,0,49,51,3,4,2,6,50,41,1,0,0,0,50,44,1,0,0,0,50,
        47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,5,1,0,0,
        0,54,52,1,0,0,0,55,56,5,10,0,0,56,57,3,4,2,0,57,7,1,0,0,0,58,59,
        5,2,0,0,59,60,3,4,2,0,60,61,5,3,0,0,61,62,3,2,1,0,62,9,1,0,0,0,63,
        64,5,6,0,0,64,65,3,4,2,0,65,66,5,7,0,0,66,69,3,2,1,0,67,68,5,8,0,
        0,68,70,3,2,1,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,
        5,9,0,0,72,11,1,0,0,0,6,15,29,39,50,52,69
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'while'", "'do'", "'and'", 
                     "'or'", "'if'", "'then'", "'else'", "'fi'", "'print'", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "'*'", 
                     "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "TEXT", "WHILE", "DO", "AND", "OR", "IF", 
                      "THEN", "ELSE", "FI", "PRINT", "EQUAL", "INT", "NEWLINE", 
                      "ID", "MUL", "DIV", "PLUS", "MIN", "OPENPARENS", "CLOSINGPARENS", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_print = 3
    RULE_loop = 4
    RULE_ifStat = 5

    ruleNames =  [ "prog", "statement", "expr", "print", "loop", "ifStat" ]

    EOF = Token.EOF
    TEXT=1
    WHILE=2
    DO=3
    AND=4
    OR=5
    IF=6
    THEN=7
    ELSE=8
    FI=9
    PRINT=10
    EQUAL=11
    INT=12
    NEWLINE=13
    ID=14
    MUL=15
    DIV=16
    PLUS=17
    MIN=18
    OPENPARENS=19
    CLOSINGPARENS=20
    WS=21

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MyGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 554054) != 0):
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


        def getRuleIndex(self):
            return MyGrammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintLineContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MyGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintLine" ):
                listener.enterPrintLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintLine" ):
                listener.exitPrintLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintLine" ):
                return visitor.visitPrintLine(self)
            else:
                return visitor.visitChildren(self)


    class LoopExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def loop(self):
            return self.getTypedRuleContext(MyGrammarParser.LoopContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopExpr" ):
                listener.enterLoopExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopExpr" ):
                listener.exitLoopExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopExpr" ):
                return visitor.visitLoopExpr(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(MyGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class IfExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStat(self):
            return self.getTypedRuleContext(MyGrammarParser.IfStatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)
        def EQUAL(self):
            return self.getToken(MyGrammarParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MyGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def print_(self):
            return self.getTypedRuleContext(MyGrammarParser.PrintContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.PrintLineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(MyGrammarParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(MyGrammarParser.ID)
                self.state = 21
                self.match(MyGrammarParser.EQUAL)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(MyGrammarParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(MyGrammarParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.print_()
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.IfExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.ifStat()
                pass

            elif la_ == 6:
                localctx = MyGrammarParser.LoopExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.loop()
                pass


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


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class TextContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(MyGrammarParser.TEXT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)


    class OperationContext(ExprContext):

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

        def MUL(self):
            return self.getToken(MyGrammarParser.MUL, 0)
        def DIV(self):
            return self.getToken(MyGrammarParser.DIV, 0)
        def PLUS(self):
            return self.getToken(MyGrammarParser.PLUS, 0)
        def MIN(self):
            return self.getToken(MyGrammarParser.MIN, 0)
        def AND(self):
            return self.getToken(MyGrammarParser.AND, 0)
        def OR(self):
            return self.getToken(MyGrammarParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = MyGrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 32
                self.match(MyGrammarParser.INT)
                pass
            elif token in [14]:
                localctx = MyGrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(MyGrammarParser.ID)
                pass
            elif token in [19]:
                localctx = MyGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass
            elif token in [1]:
                localctx = MyGrammarParser.TextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(MyGrammarParser.TEXT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MyGrammarParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = MyGrammarParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MyGrammarParser.PRINT)
            self.state = 56
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyGrammarParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def DO(self):
            return self.getToken(MyGrammarParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(MyGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MyGrammarParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MyGrammarParser.WHILE)
            self.state = 59
            self.expr(0)
            self.state = 60
            self.match(MyGrammarParser.DO)
            self.state = 61
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyGrammarParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def THEN(self):
            return self.getToken(MyGrammarParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def FI(self):
            return self.getToken(MyGrammarParser.FI, 0)

        def ELSE(self):
            return self.getToken(MyGrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_ifStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = MyGrammarParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MyGrammarParser.IF)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.match(MyGrammarParser.THEN)
            self.state = 66
            self.statement()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 67
                self.match(MyGrammarParser.ELSE)
                self.state = 68
                self.statement()


            self.state = 71
            self.match(MyGrammarParser.FI)
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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




