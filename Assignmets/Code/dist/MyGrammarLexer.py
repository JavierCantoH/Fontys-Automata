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
        4,0,21,126,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,1,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,11,4,11,94,8,11,11,11,12,11,95,1,12,
        3,12,99,8,12,1,12,1,12,1,13,4,13,104,8,13,11,13,12,13,105,1,14,1,
        14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,4,20,121,
        8,20,11,20,12,20,122,1,20,1,20,0,0,21,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,1,0,4,3,0,10,10,13,13,34,34,1,0,48,57,2,0,65,90,
        97,122,3,0,9,10,13,13,32,32,130,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,1,43,1,0,0,0,3,52,1,0,0,
        0,5,58,1,0,0,0,7,61,1,0,0,0,9,65,1,0,0,0,11,68,1,0,0,0,13,71,1,0,
        0,0,15,76,1,0,0,0,17,81,1,0,0,0,19,84,1,0,0,0,21,90,1,0,0,0,23,93,
        1,0,0,0,25,98,1,0,0,0,27,103,1,0,0,0,29,107,1,0,0,0,31,109,1,0,0,
        0,33,111,1,0,0,0,35,113,1,0,0,0,37,115,1,0,0,0,39,117,1,0,0,0,41,
        120,1,0,0,0,43,47,5,34,0,0,44,46,8,0,0,0,45,44,1,0,0,0,46,49,1,0,
        0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,
        5,34,0,0,51,2,1,0,0,0,52,53,5,119,0,0,53,54,5,104,0,0,54,55,5,105,
        0,0,55,56,5,108,0,0,56,57,5,101,0,0,57,4,1,0,0,0,58,59,5,100,0,0,
        59,60,5,111,0,0,60,6,1,0,0,0,61,62,5,97,0,0,62,63,5,110,0,0,63,64,
        5,100,0,0,64,8,1,0,0,0,65,66,5,111,0,0,66,67,5,114,0,0,67,10,1,0,
        0,0,68,69,5,105,0,0,69,70,5,102,0,0,70,12,1,0,0,0,71,72,5,116,0,
        0,72,73,5,104,0,0,73,74,5,101,0,0,74,75,5,110,0,0,75,14,1,0,0,0,
        76,77,5,101,0,0,77,78,5,108,0,0,78,79,5,115,0,0,79,80,5,101,0,0,
        80,16,1,0,0,0,81,82,5,102,0,0,82,83,5,105,0,0,83,18,1,0,0,0,84,85,
        5,112,0,0,85,86,5,114,0,0,86,87,5,105,0,0,87,88,5,110,0,0,88,89,
        5,116,0,0,89,20,1,0,0,0,90,91,5,61,0,0,91,22,1,0,0,0,92,94,7,1,0,
        0,93,92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,24,
        1,0,0,0,97,99,5,13,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,
        0,100,101,5,10,0,0,101,26,1,0,0,0,102,104,7,2,0,0,103,102,1,0,0,
        0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,28,1,0,0,0,
        107,108,5,42,0,0,108,30,1,0,0,0,109,110,5,47,0,0,110,32,1,0,0,0,
        111,112,5,43,0,0,112,34,1,0,0,0,113,114,5,45,0,0,114,36,1,0,0,0,
        115,116,5,40,0,0,116,38,1,0,0,0,117,118,5,41,0,0,118,40,1,0,0,0,
        119,121,7,3,0,0,120,119,1,0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,
        122,123,1,0,0,0,123,124,1,0,0,0,124,125,6,20,0,0,125,42,1,0,0,0,
        6,0,47,95,98,105,122,1,6,0,0
    ]

class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TEXT = 1
    WHILE = 2
    DO = 3
    AND = 4
    OR = 5
    IF = 6
    THEN = 7
    ELSE = 8
    FI = 9
    PRINT = 10
    EQUAL = 11
    INT = 12
    NEWLINE = 13
    ID = 14
    MUL = 15
    DIV = 16
    PLUS = 17
    MIN = 18
    OPENPARENS = 19
    CLOSINGPARENS = 20
    WS = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'while'", "'do'", "'and'", "'or'", "'if'", "'then'", "'else'", 
            "'fi'", "'print'", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
            "')'" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "WHILE", "DO", "AND", "OR", "IF", "THEN", "ELSE", "FI", 
            "PRINT", "EQUAL", "INT", "NEWLINE", "ID", "MUL", "DIV", "PLUS", 
            "MIN", "OPENPARENS", "CLOSINGPARENS", "WS" ]

    ruleNames = [ "TEXT", "WHILE", "DO", "AND", "OR", "IF", "THEN", "ELSE", 
                  "FI", "PRINT", "EQUAL", "INT", "NEWLINE", "ID", "MUL", 
                  "DIV", "PLUS", "MIN", "OPENPARENS", "CLOSINGPARENS", "WS" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


