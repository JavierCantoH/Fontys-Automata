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
        4,0,11,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,
        45,8,8,11,8,12,8,46,1,9,4,9,50,8,9,11,9,12,9,51,1,10,4,10,55,8,10,
        11,10,12,10,56,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,1,0,3,2,0,65,90,97,122,1,0,48,57,2,0,9,10,32,
        32,62,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,1,23,1,0,0,0,3,25,1,0,0,0,5,31,1,0,0,0,7,33,1,0,0,
        0,9,35,1,0,0,0,11,37,1,0,0,0,13,39,1,0,0,0,15,41,1,0,0,0,17,44,1,
        0,0,0,19,49,1,0,0,0,21,54,1,0,0,0,23,24,5,61,0,0,24,2,1,0,0,0,25,
        26,5,112,0,0,26,27,5,114,0,0,27,28,5,105,0,0,28,29,5,110,0,0,29,
        30,5,116,0,0,30,4,1,0,0,0,31,32,5,40,0,0,32,6,1,0,0,0,33,34,5,41,
        0,0,34,8,1,0,0,0,35,36,5,43,0,0,36,10,1,0,0,0,37,38,5,45,0,0,38,
        12,1,0,0,0,39,40,5,42,0,0,40,14,1,0,0,0,41,42,5,47,0,0,42,16,1,0,
        0,0,43,45,7,0,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,18,1,0,0,0,48,50,7,1,0,0,49,48,1,0,0,0,50,51,1,0,0,0,
        51,49,1,0,0,0,51,52,1,0,0,0,52,20,1,0,0,0,53,55,7,2,0,0,54,53,1,
        0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,
        59,6,10,0,0,59,22,1,0,0,0,4,0,46,51,56,1,6,0,0
    ]

class NumericalExpressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    VariableName = 9
    Number = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'print'", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "VariableName", "Number", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "VariableName", "Number", "WS" ]

    grammarFileName = "NumericalExpression.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


