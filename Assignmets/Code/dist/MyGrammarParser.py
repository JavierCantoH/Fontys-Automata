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
        4,1,35,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,1,1,1,1,1,3,1,32,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,45,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,57,
        8,1,1,2,1,2,1,2,1,2,3,2,63,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,73,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,93,8,2,10,2,12,2,96,9,2,1,3,1,3,1,3,1,3,3,3,
        102,8,3,1,3,1,3,1,3,1,4,1,4,5,4,109,8,4,10,4,12,4,112,9,4,1,4,1,
        4,1,5,1,5,1,5,5,5,119,8,5,10,5,12,5,122,9,5,1,6,1,6,1,6,1,7,1,7,
        1,7,5,7,130,8,7,10,7,12,7,133,9,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,149,8,10,1,10,0,1,4,11,0,2,
        4,6,8,10,12,14,16,18,20,0,7,1,0,21,22,1,0,25,26,1,0,27,28,1,0,14,
        15,1,0,5,6,1,0,7,8,1,0,9,10,167,0,25,1,0,0,0,2,56,1,0,0,0,4,72,1,
        0,0,0,6,97,1,0,0,0,8,106,1,0,0,0,10,115,1,0,0,0,12,123,1,0,0,0,14,
        126,1,0,0,0,16,134,1,0,0,0,18,137,1,0,0,0,20,142,1,0,0,0,22,24,3,
        2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,
        1,1,0,0,0,27,25,1,0,0,0,28,57,3,6,3,0,29,31,5,1,0,0,30,32,3,4,2,
        0,31,30,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,57,5,4,0,0,34,35,
        3,4,2,0,35,36,5,4,0,0,36,57,1,0,0,0,37,38,3,4,2,0,38,39,5,23,0,0,
        39,57,1,0,0,0,40,41,5,3,0,0,41,44,5,24,0,0,42,43,5,20,0,0,43,45,
        3,4,2,0,44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,57,5,4,0,0,
        47,48,5,24,0,0,48,49,5,20,0,0,49,50,3,4,2,0,50,51,5,4,0,0,51,57,
        1,0,0,0,52,57,5,23,0,0,53,57,3,16,8,0,54,57,3,20,10,0,55,57,3,18,
        9,0,56,28,1,0,0,0,56,29,1,0,0,0,56,34,1,0,0,0,56,37,1,0,0,0,56,40,
        1,0,0,0,56,47,1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,0,
        56,55,1,0,0,0,57,3,1,0,0,0,58,59,6,2,-1,0,59,60,5,24,0,0,60,62,5,
        29,0,0,61,63,3,14,7,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,
        64,73,5,30,0,0,65,73,7,0,0,0,66,73,5,24,0,0,67,68,5,29,0,0,68,69,
        3,4,2,0,69,70,5,30,0,0,70,73,1,0,0,0,71,73,5,11,0,0,72,58,1,0,0,
        0,72,65,1,0,0,0,72,66,1,0,0,0,72,67,1,0,0,0,72,71,1,0,0,0,73,94,
        1,0,0,0,74,75,10,10,0,0,75,76,7,1,0,0,76,93,3,4,2,11,77,78,10,9,
        0,0,78,79,7,2,0,0,79,93,3,4,2,10,80,81,10,8,0,0,81,82,7,3,0,0,82,
        93,3,4,2,9,83,84,10,7,0,0,84,85,7,4,0,0,85,93,3,4,2,8,86,87,10,6,
        0,0,87,88,7,5,0,0,88,93,3,4,2,7,89,90,10,5,0,0,90,91,7,6,0,0,91,
        93,3,4,2,6,92,74,1,0,0,0,92,77,1,0,0,0,92,80,1,0,0,0,92,83,1,0,0,
        0,92,86,1,0,0,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,
        1,0,0,0,95,5,1,0,0,0,96,94,1,0,0,0,97,98,5,3,0,0,98,99,5,24,0,0,
        99,101,5,29,0,0,100,102,3,10,5,0,101,100,1,0,0,0,101,102,1,0,0,0,
        102,103,1,0,0,0,103,104,5,30,0,0,104,105,3,8,4,0,105,7,1,0,0,0,106,
        110,5,31,0,0,107,109,3,2,1,0,108,107,1,0,0,0,109,112,1,0,0,0,110,
        108,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,
        114,5,32,0,0,114,9,1,0,0,0,115,120,3,12,6,0,116,117,5,2,0,0,117,
        119,3,12,6,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,
        121,1,0,0,0,121,11,1,0,0,0,122,120,1,0,0,0,123,124,5,3,0,0,124,125,
        5,24,0,0,125,13,1,0,0,0,126,131,3,4,2,0,127,128,5,2,0,0,128,130,
        3,4,2,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,15,1,0,0,0,133,131,1,0,0,0,134,135,5,19,0,0,135,136,
        3,4,2,0,136,17,1,0,0,0,137,138,5,12,0,0,138,139,3,4,2,0,139,140,
        5,13,0,0,140,141,3,2,1,0,141,19,1,0,0,0,142,143,5,16,0,0,143,144,
        3,4,2,0,144,145,5,17,0,0,145,148,3,2,1,0,146,147,5,18,0,0,147,149,
        3,2,1,0,148,146,1,0,0,0,148,149,1,0,0,0,149,21,1,0,0,0,13,25,31,
        44,56,62,72,92,94,101,110,120,131,148
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "','", "<INVALID>", "';'", 
                     "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", "<INVALID>", 
                     "'while'", "'do'", "'and'", "'or'", "'if'", "'then'", 
                     "'else'", "'print'", "'='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "'/'", "'+'", "'-'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "RETURN", "COMMA", "TYPE", "SEMICOLON", 
                      "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL", 
                      "BOOLEAN_EQUAL", "BOOLEAN_NOT_EQUAL", "TEXT", "WHILE", 
                      "DO", "AND", "OR", "IF", "THEN", "ELSE", "PRINT", 
                      "EQUAL", "INT", "FLOAT", "NEWLINE", "ID", "MUL", "DIV", 
                      "PLUS", "MIN", "OPENPARENS", "CLOSINGPARENS", "OPENCURLYB", 
                      "CLOSINGCURLYB", "OPENSQUAREB", "CLOSINGSQUAREB", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_functionDecl = 3
    RULE_block = 4
    RULE_formalParameters = 5
    RULE_formalParameter = 6
    RULE_exprList = 7
    RULE_print = 8
    RULE_loop = 9
    RULE_ifStat = 10

    ruleNames =  [ "prog", "statement", "expr", "functionDecl", "block", 
                   "formalParameters", "formalParameter", "exprList", "print", 
                   "loop", "ifStat" ]

    EOF = Token.EOF
    RETURN=1
    COMMA=2
    TYPE=3
    SEMICOLON=4
    GREATER=5
    LESS=6
    GREATER_EQUAL=7
    LESS_EQUAL=8
    BOOLEAN_EQUAL=9
    BOOLEAN_NOT_EQUAL=10
    TEXT=11
    WHILE=12
    DO=13
    AND=14
    OR=15
    IF=16
    THEN=17
    ELSE=18
    PRINT=19
    EQUAL=20
    INT=21
    FLOAT=22
    NEWLINE=23
    ID=24
    MUL=25
    DIV=26
    PLUS=27
    MIN=28
    OPENPARENS=29
    CLOSINGPARENS=30
    OPENCURLYB=31
    CLOSINGCURLYB=32
    OPENSQUAREB=33
    CLOSINGSQUAREB=34
    WS=35

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 568924170) != 0:
                self.state = 22
                self.statement()
                self.state = 27
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


    class ReturnFuncContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MyGrammarParser.RETURN, 0)
        def SEMICOLON(self):
            return self.getToken(MyGrammarParser.SEMICOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnFunc" ):
                listener.enterReturnFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnFunc" ):
                listener.exitReturnFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnFunc" ):
                return visitor.visitReturnFunc(self)
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


    class CallingFuncContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(MyGrammarParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallingFunc" ):
                listener.enterCallingFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallingFunc" ):
                listener.exitCallingFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallingFunc" ):
                return visitor.visitCallingFunc(self)
            else:
                return visitor.visitChildren(self)


    class FunctionDeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionDecl(self):
            return self.getTypedRuleContext(MyGrammarParser.FunctionDeclContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
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
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.FunctionDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.functionDecl()
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.ReturnFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(MyGrammarParser.RETURN)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 559941632) != 0:
                    self.state = 30
                    self.expr(0)


                self.state = 33
                self.match(MyGrammarParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.CallingFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(MyGrammarParser.SEMICOLON)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.PrintLineContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(MyGrammarParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.match(MyGrammarParser.TYPE)
                self.state = 41
                self.match(MyGrammarParser.ID)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 42
                    self.match(MyGrammarParser.EQUAL)
                    self.state = 43
                    self.expr(0)


                self.state = 46
                self.match(MyGrammarParser.SEMICOLON)
                pass

            elif la_ == 6:
                localctx = MyGrammarParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.match(MyGrammarParser.ID)
                self.state = 48
                self.match(MyGrammarParser.EQUAL)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(MyGrammarParser.SEMICOLON)
                pass

            elif la_ == 7:
                localctx = MyGrammarParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.match(MyGrammarParser.NEWLINE)
                pass

            elif la_ == 8:
                localctx = MyGrammarParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.print_()
                pass

            elif la_ == 9:
                localctx = MyGrammarParser.IfExprContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.ifStat()
                pass

            elif la_ == 10:
                localctx = MyGrammarParser.LoopExprContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 55
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


    class ExprFuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)
        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)
        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)
        def exprList(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprFuncCall" ):
                listener.enterExprFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprFuncCall" ):
                listener.exitExprFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFuncCall" ):
                return visitor.visitExprFuncCall(self)
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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.ExprFuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 59
                self.match(MyGrammarParser.ID)
                self.state = 60
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 559941632) != 0:
                    self.state = 61
                    self.exprList()


                self.state = 64
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(MyGrammarParser.ID)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.match(MyGrammarParser.OPENPARENS)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(MyGrammarParser.CLOSINGPARENS)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.TextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(MyGrammarParser.TEXT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 75
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 76
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 78
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 79
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 81
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 82
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 84
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 87
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OperationContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 90
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MyGrammarParser.TYPE, 0)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def OPENPARENS(self):
            return self.getToken(MyGrammarParser.OPENPARENS, 0)

        def CLOSINGPARENS(self):
            return self.getToken(MyGrammarParser.CLOSINGPARENS, 0)

        def block(self):
            return self.getTypedRuleContext(MyGrammarParser.BlockContext,0)


        def formalParameters(self):
            return self.getTypedRuleContext(MyGrammarParser.FormalParametersContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = MyGrammarParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MyGrammarParser.TYPE)
            self.state = 98
            self.match(MyGrammarParser.ID)
            self.state = 99
            self.match(MyGrammarParser.OPENPARENS)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 100
                self.formalParameters()


            self.state = 103
            self.match(MyGrammarParser.CLOSINGPARENS)
            self.state = 104
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENCURLYB(self):
            return self.getToken(MyGrammarParser.OPENCURLYB, 0)

        def CLOSINGCURLYB(self):
            return self.getToken(MyGrammarParser.CLOSINGCURLYB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MyGrammarParser.OPENCURLYB)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 568924170) != 0:
                self.state = 107
                self.statement()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(MyGrammarParser.CLOSINGCURLYB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.FormalParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.COMMA)
            else:
                return self.getToken(MyGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_formalParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameters" ):
                listener.enterFormalParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameters" ):
                listener.exitFormalParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameters" ):
                return visitor.visitFormalParameters(self)
            else:
                return visitor.visitChildren(self)




    def formalParameters(self):

        localctx = MyGrammarParser.FormalParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.formalParameter()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 116
                self.match(MyGrammarParser.COMMA)
                self.state = 117
                self.formalParameter()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MyGrammarParser.TYPE, 0)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameter" ):
                return visitor.visitFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def formalParameter(self):

        localctx = MyGrammarParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MyGrammarParser.TYPE)
            self.state = 124
            self.match(MyGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.COMMA)
            else:
                return self.getToken(MyGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = MyGrammarParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.expr(0)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 127
                self.match(MyGrammarParser.COMMA)
                self.state = 128
                self.expr(0)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 16, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(MyGrammarParser.PRINT)
            self.state = 135
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
        self.enterRule(localctx, 18, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MyGrammarParser.WHILE)
            self.state = 138
            self.expr(0)
            self.state = 139
            self.match(MyGrammarParser.DO)
            self.state = 140
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
        self.enterRule(localctx, 20, self.RULE_ifStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MyGrammarParser.IF)
            self.state = 143
            self.expr(0)
            self.state = 144
            self.match(MyGrammarParser.THEN)
            self.state = 145
            self.statement()
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(MyGrammarParser.ELSE)
                self.state = 147
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
         




