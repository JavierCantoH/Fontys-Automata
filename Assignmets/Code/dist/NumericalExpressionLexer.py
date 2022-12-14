# Generated from NumericalExpression.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,59,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,4,1,27,8,1,11,
        1,12,1,28,1,2,3,2,32,8,2,1,2,1,2,1,3,4,3,37,8,3,11,3,12,3,38,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,54,8,10,11,
        10,12,10,55,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        17,9,19,10,21,11,1,0,3,1,0,48,57,2,0,65,90,97,122,2,0,9,9,32,32,
        62,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,
        21,1,0,0,0,1,23,1,0,0,0,3,26,1,0,0,0,5,31,1,0,0,0,7,36,1,0,0,0,9,
        40,1,0,0,0,11,42,1,0,0,0,13,44,1,0,0,0,15,46,1,0,0,0,17,48,1,0,0,
        0,19,50,1,0,0,0,21,53,1,0,0,0,23,24,5,61,0,0,24,2,1,0,0,0,25,27,
        7,0,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,
        29,4,1,0,0,0,30,32,5,13,0,0,31,30,1,0,0,0,31,32,1,0,0,0,32,33,1,
        0,0,0,33,34,5,10,0,0,34,6,1,0,0,0,35,37,7,1,0,0,36,35,1,0,0,0,37,
        38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,8,1,0,0,0,40,41,5,42,0,
        0,41,10,1,0,0,0,42,43,5,47,0,0,43,12,1,0,0,0,44,45,5,43,0,0,45,14,
        1,0,0,0,46,47,5,45,0,0,47,16,1,0,0,0,48,49,5,40,0,0,49,18,1,0,0,
        0,50,51,5,41,0,0,51,20,1,0,0,0,52,54,7,2,0,0,53,52,1,0,0,0,54,55,
        1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,6,10,0,0,
        58,22,1,0,0,0,5,0,28,31,38,55,1,6,0,0
    ]

class NumericalExpressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQUAL = 1
    INT = 2
    NEWLINE = 3
    ID = 4
    MUL = 5
    DIV = 6
    PLUS = 7
    MIN = 8
    OPENPARENS = 9
    CLOSINGPARENS = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "EQUAL", "INT", "NEWLINE", "ID", "MUL", "DIV", "PLUS", "MIN", 
            "OPENPARENS", "CLOSINGPARENS", "WS" ]

    ruleNames = [ "EQUAL", "INT", "NEWLINE", "ID", "MUL", "DIV", "PLUS", 
                  "MIN", "OPENPARENS", "CLOSINGPARENS", "WS" ]

    grammarFileName = "NumericalExpression.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


