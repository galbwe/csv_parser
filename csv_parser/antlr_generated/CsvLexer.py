# Generated from Csv.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("\64\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\6\3\25\n\3\r\3\16\3\26\3\4\3\4")
        buf.write("\3\4\6\4\34\n\4\r\4\16\4\35\3\5\3\5\7\5\"\n\5\f\5\16\5")
        buf.write("%\13\5\3\5\3\5\3\6\6\6*\n\6\r\6\16\6+\3\7\3\7\3\b\6\b")
        buf.write("\61\n\b\r\b\16\b\62\2\2\t\3\2\5\3\7\4\t\5\13\6\r\7\17")
        buf.write("\b\3\2\7\3\2\62;\4\2$$))\5\2\"\"C\\c|\4\2\f\f\17\17\4")
        buf.write("\2\13\13\"\"\2\67\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5")
        buf.write("\24\3\2\2\2\7\30\3\2\2\2\t\37\3\2\2\2\13)\3\2\2\2\r-\3")
        buf.write("\2\2\2\17\60\3\2\2\2\21\22\t\2\2\2\22\4\3\2\2\2\23\25")
        buf.write("\5\3\2\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26")
        buf.write("\27\3\2\2\2\27\6\3\2\2\2\30\31\5\3\2\2\31\33\7\60\2\2")
        buf.write("\32\34\5\3\2\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2")
        buf.write("\2\35\36\3\2\2\2\36\b\3\2\2\2\37#\t\3\2\2 \"\t\4\2\2!")
        buf.write(" \3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%#\3")
        buf.write("\2\2\2&\'\t\3\2\2\'\n\3\2\2\2(*\t\5\2\2)(\3\2\2\2*+\3")
        buf.write("\2\2\2+)\3\2\2\2+,\3\2\2\2,\f\3\2\2\2-.\7.\2\2.\16\3\2")
        buf.write("\2\2/\61\t\6\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2")
        buf.write("\2\62\63\3\2\2\2\63\20\3\2\2\2\t\2\26\35!#+\62\2")
        return buf.getvalue()


class CsvLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    FLOAT = 2
    STRING = 3
    NEWLINE = 4
    SEPARATOR = 5
    WHITESPACE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "STRING", "NEWLINE", "SEPARATOR", "WHITESPACE" ]

    ruleNames = [ "DIGIT", "INTEGER", "FLOAT", "STRING", "NEWLINE", "SEPARATOR", 
                  "WHITESPACE" ]

    grammarFileName = "Csv.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


