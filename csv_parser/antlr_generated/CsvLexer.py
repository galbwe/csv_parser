# Generated from Csv.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(")\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\6\3\23\n\3\r\3\16\3\24\3\4\3\4\3\4\6\4\32")
        buf.write("\n\4\r\4\16\4\33\3\5\6\5\37\n\5\r\5\16\5 \3\6\3\6\3\7")
        buf.write("\6\7&\n\7\r\7\16\7\'\2\2\b\3\2\5\3\7\4\t\5\13\6\r\7\3")
        buf.write("\2\5\3\2\62;\4\2\f\f\17\17\4\2\13\13\"\"\2+\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3")
        buf.write("\17\3\2\2\2\5\22\3\2\2\2\7\26\3\2\2\2\t\36\3\2\2\2\13")
        buf.write("\"\3\2\2\2\r%\3\2\2\2\17\20\t\2\2\2\20\4\3\2\2\2\21\23")
        buf.write("\5\3\2\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25\6\3\2\2\2\26\27\5\3\2\2\27\31\7\60\2\2")
        buf.write("\30\32\5\3\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2")
        buf.write("\2\33\34\3\2\2\2\34\b\3\2\2\2\35\37\t\3\2\2\36\35\3\2")
        buf.write("\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\n\3\2\2\2\"#\7")
        buf.write(".\2\2#\f\3\2\2\2$&\t\4\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2")
        buf.write("\2\2\'(\3\2\2\2(\16\3\2\2\2\7\2\24\33 \'\2")
        return buf.getvalue()


class CsvLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    FLOAT = 2
    NEWLINE = 3
    SEPARATOR = 4
    WHITESPACE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "NEWLINE", "SEPARATOR", "WHITESPACE" ]

    ruleNames = [ "DIGIT", "INTEGER", "FLOAT", "NEWLINE", "SEPARATOR", "WHITESPACE" ]

    grammarFileName = "Csv.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


