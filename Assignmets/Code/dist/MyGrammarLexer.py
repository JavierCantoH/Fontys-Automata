# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,71,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,39,8,3,11,3,12,3,40,
        1,4,3,4,44,8,4,1,4,1,4,1,5,4,5,49,8,5,11,5,12,5,50,1,6,1,6,1,7,1,
        7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,4,12,66,8,12,11,12,12,
        12,67,1,12,1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,1,0,3,1,0,48,57,2,0,65,90,97,122,2,0,9,9,32,
        32,74,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,33,1,0,0,
        0,5,35,1,0,0,0,7,38,1,0,0,0,9,43,1,0,0,0,11,48,1,0,0,0,13,52,1,0,
        0,0,15,54,1,0,0,0,17,56,1,0,0,0,19,58,1,0,0,0,21,60,1,0,0,0,23,62,
        1,0,0,0,25,65,1,0,0,0,27,28,5,112,0,0,28,29,5,114,0,0,29,30,5,105,
        0,0,30,31,5,110,0,0,31,32,5,116,0,0,32,2,1,0,0,0,33,34,5,44,0,0,
        34,4,1,0,0,0,35,36,5,61,0,0,36,6,1,0,0,0,37,39,7,0,0,0,38,37,1,0,
        0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,8,1,0,0,0,42,44,
        5,13,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,10,0,
        0,46,10,1,0,0,0,47,49,7,1,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,
        1,0,0,0,50,51,1,0,0,0,51,12,1,0,0,0,52,53,5,42,0,0,53,14,1,0,0,0,
        54,55,5,47,0,0,55,16,1,0,0,0,56,57,5,43,0,0,57,18,1,0,0,0,58,59,
        5,45,0,0,59,20,1,0,0,0,60,61,5,40,0,0,61,22,1,0,0,0,62,63,5,41,0,
        0,63,24,1,0,0,0,64,66,7,2,0,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,
        1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,6,12,0,0,70,26,1,0,0,0,
        5,0,40,43,50,67,1,6,0,0
    ]

class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    COMMA = 2
    EQUAL = 3
    INT = 4
    NEWLINE = 5
    ID = 6
    MUL = 7
    DIV = 8
    PLUS = 9
    MIN = 10
    OPENPARENS = 11
    CLOSINGPARENS = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "','", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
            "')'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "COMMA", "EQUAL", "INT", "NEWLINE", "ID", "MUL", "DIV", 
            "PLUS", "MIN", "OPENPARENS", "CLOSINGPARENS", "WS" ]

    ruleNames = [ "PRINT", "COMMA", "EQUAL", "INT", "NEWLINE", "ID", "MUL", 
                  "DIV", "PLUS", "MIN", "OPENPARENS", "CLOSINGPARENS", "WS" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

