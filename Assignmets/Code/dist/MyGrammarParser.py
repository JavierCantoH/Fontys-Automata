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
        4,1,29,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,67,8,2,10,2,12,2,70,9,2,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,86,8,5,1,
        5,0,1,4,6,0,2,4,6,8,10,0,7,1,0,19,20,1,0,23,24,1,0,25,26,1,0,12,
        13,1,0,3,4,1,0,5,6,1,0,7,8,99,0,13,1,0,0,0,2,36,1,0,0,0,4,46,1,0,
        0,0,6,71,1,0,0,0,8,74,1,0,0,0,10,79,1,0,0,0,12,14,3,2,1,0,13,12,
        1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,
        18,3,4,2,0,18,19,5,21,0,0,19,37,1,0,0,0,20,21,5,1,0,0,21,24,5,22,
        0,0,22,23,5,18,0,0,23,25,3,4,2,0,24,22,1,0,0,0,24,25,1,0,0,0,25,
        26,1,0,0,0,26,37,5,2,0,0,27,28,5,22,0,0,28,29,5,18,0,0,29,30,3,4,
        2,0,30,31,5,2,0,0,31,37,1,0,0,0,32,37,5,21,0,0,33,37,3,6,3,0,34,
        37,3,10,5,0,35,37,3,8,4,0,36,17,1,0,0,0,36,20,1,0,0,0,36,27,1,0,
        0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,3,
        1,0,0,0,38,39,6,2,-1,0,39,47,7,0,0,0,40,47,5,22,0,0,41,42,5,27,0,
        0,42,43,3,4,2,0,43,44,5,28,0,0,44,47,1,0,0,0,45,47,5,9,0,0,46,38,
        1,0,0,0,46,40,1,0,0,0,46,41,1,0,0,0,46,45,1,0,0,0,47,68,1,0,0,0,
        48,49,10,10,0,0,49,50,7,1,0,0,50,67,3,4,2,11,51,52,10,9,0,0,52,53,
        7,2,0,0,53,67,3,4,2,10,54,55,10,8,0,0,55,56,7,3,0,0,56,67,3,4,2,
        9,57,58,10,7,0,0,58,59,7,4,0,0,59,67,3,4,2,8,60,61,10,6,0,0,61,62,
        7,5,0,0,62,67,3,4,2,7,63,64,10,5,0,0,64,65,7,6,0,0,65,67,3,4,2,6,
        66,48,1,0,0,0,66,51,1,0,0,0,66,54,1,0,0,0,66,57,1,0,0,0,66,60,1,
        0,0,0,66,63,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        5,1,0,0,0,70,68,1,0,0,0,71,72,5,17,0,0,72,73,3,4,2,0,73,7,1,0,0,
        0,74,75,5,10,0,0,75,76,3,4,2,0,76,77,5,11,0,0,77,78,3,2,1,0,78,9,
        1,0,0,0,79,80,5,14,0,0,80,81,3,4,2,0,81,82,5,15,0,0,82,85,3,2,1,
        0,83,84,5,16,0,0,84,86,3,2,1,0,85,83,1,0,0,0,85,86,1,0,0,0,86,11,
        1,0,0,0,7,15,24,36,46,66,68,85
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "';'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "<INVALID>", "'while'", "'do'", 
                     "'and'", "'or'", "'if'", "'then'", "'else'", "'print'", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "TYPE", "SEMICOLON", "GREATER", "LESS", 
                      "GREATER_EQUAL", "LESS_EQUAL", "BOOLEAN_EQUAL", "BOOLEAN_NOT_EQUAL", 
                      "TEXT", "WHILE", "DO", "AND", "OR", "IF", "THEN", 
                      "ELSE", "PRINT", "EQUAL", "INT", "FLOAT", "NEWLINE", 
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
    TYPE=1
    SEMICOLON=2
    GREATER=3
    LESS=4
    GREATER_EQUAL=5
    LESS_EQUAL=6
    BOOLEAN_EQUAL=7
    BOOLEAN_NOT_EQUAL=8
    TEXT=9
    WHILE=10
    DO=11
    AND=12
    OR=13
    IF=14
    THEN=15
    ELSE=16
    PRINT=17
    EQUAL=18
    INT=19
    FLOAT=20
    NEWLINE=21
    ID=22
    MUL=23
    DIV=24
    PLUS=25
    MIN=26
    OPENPARENS=27
    CLOSINGPARENS=28
    WS=29

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
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 142231042) != 0):
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


    class AssignExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)
        def EQUAL(self):
            return self.getToken(MyGrammarParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(MyGrammarParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(MyGrammarParser.TYPE, 0)
        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)
        def SEMICOLON(self):
            return self.getToken(MyGrammarParser.SEMICOLON, 0)
        def EQUAL(self):
            return self.getToken(MyGrammarParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
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
                self.match(MyGrammarParser.TYPE)
                self.state = 21
                self.match(MyGrammarParser.ID)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 22
                    self.match(MyGrammarParser.EQUAL)
                    self.state = 23
                    self.expr(0)


                self.state = 26
                self.match(MyGrammarParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(MyGrammarParser.ID)
                self.state = 28
                self.match(MyGrammarParser.EQUAL)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(MyGrammarParser.SEMICOLON)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(MyGrammarParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.print_()
                pass

            elif la_ == 6:
                localctx = MyGrammarParser.IfExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 34
                self.ifStat()
                pass

            elif la_ == 7:
                localctx = MyGrammarParser.LoopExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 35
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


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)
        def FLOAT(self):
            return self.getToken(MyGrammarParser.FLOAT, 0)

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
        def GREATER(self):
            return self.getToken(MyGrammarParser.GREATER, 0)
        def LESS(self):
            return self.getToken(MyGrammarParser.LESS, 0)
        def GREATER_EQUAL(self):
            return self.getToken(MyGrammarParser.GREATER_EQUAL, 0)
        def LESS_EQUAL(self):
            return self.getToken(MyGrammarParser.LESS_EQUAL, 0)
        def BOOLEAN_EQUAL(self):
            return self.getToken(MyGrammarParser.BOOLEAN_EQUAL, 0)
        def BOOLEAN_NOT_EQUAL(self):
            return self.getToken(MyGrammarParser.BOOLEAN_NOT_EQUAL, 0)

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
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20]:
                localctx = MyGrammarParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 39
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [22]:
                localctx = MyGrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(MyGrammarParser.ID)
                pass
            elif token in [27]:
                localctx = MyGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass
            elif token in [9]:
                localctx = MyGrammarParser.TextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(MyGrammarParser.TEXT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 49
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.state = 71
            self.match(MyGrammarParser.PRINT)
            self.state = 72
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
            self.state = 74
            self.match(MyGrammarParser.WHILE)
            self.state = 75
            self.expr(0)
            self.state = 76
            self.match(MyGrammarParser.DO)
            self.state = 77
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MyGrammarParser.IF)
            self.state = 80
            self.expr(0)
            self.state = 81
            self.match(MyGrammarParser.THEN)
            self.state = 82
            self.statement()
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 83
                self.match(MyGrammarParser.ELSE)
                self.state = 84
                self.statement()


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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




