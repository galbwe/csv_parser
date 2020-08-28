# Generated from Csv.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("+\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\5\3\23\n\3\3\3\6\3\26\n\3\r\3\16\3\27")
        buf.write("\3\3\5\3\33\n\3\3\3\5\3\36\n\3\3\4\5\4!\n\4\3\4\5\4$\n")
        buf.write("\4\3\4\5\4\'\n\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\3\3\2\3\5")
        buf.write("\2.\2\13\3\2\2\2\4\25\3\2\2\2\6 \3\2\2\2\b(\3\2\2\2\n")
        buf.write("\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16")
        buf.write("\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21\23")
        buf.write("\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\26\7\7\2\2\25\22\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\32\3\2\2\2\31\33\5\6\4\2\32\31\3\2\2")
        buf.write("\2\32\33\3\2\2\2\33\35\3\2\2\2\34\36\7\6\2\2\35\34\3\2")
        buf.write("\2\2\35\36\3\2\2\2\36\5\3\2\2\2\37!\7\b\2\2 \37\3\2\2")
        buf.write("\2 !\3\2\2\2!#\3\2\2\2\"$\5\b\5\2#\"\3\2\2\2#$\3\2\2\2")
        buf.write("$&\3\2\2\2%\'\7\b\2\2&%\3\2\2\2&\'\3\2\2\2\'\7\3\2\2\2")
        buf.write("()\t\2\2\2)\t\3\2\2\2\n\r\22\27\32\35 #&")
        return buf.getvalue()


class CsvParser ( Parser ):

    grammarFileName = "Csv.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "FLOAT", "STRING", "NEWLINE", 
                      "SEPARATOR", "WHITESPACE" ]

    RULE_csv = 0
    RULE_line = 1
    RULE_cell = 2
    RULE_field = 3

    ruleNames =  [ "csv", "line", "cell", "field" ]

    EOF = Token.EOF
    INTEGER=1
    FLOAT=2
    STRING=3
    NEWLINE=4
    SEPARATOR=5
    WHITESPACE=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CsvContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CsvParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsvParser.LineContext)
            else:
                return self.getTypedRuleContext(CsvParser.LineContext,i)


        def getRuleIndex(self):
            return CsvParser.RULE_csv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsv" ):
                listener.enterCsv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsv" ):
                listener.exitCsv(self)




    def csv(self):

        localctx = CsvParser.CsvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csv)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.line()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CsvParser.INTEGER) | (1 << CsvParser.FLOAT) | (1 << CsvParser.STRING) | (1 << CsvParser.SEPARATOR) | (1 << CsvParser.WHITESPACE))) != 0)):
                    break

            self.state = 13
            self.match(CsvParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(CsvParser.SEPARATOR)
            else:
                return self.getToken(CsvParser.SEPARATOR, i)

        def cell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsvParser.CellContext)
            else:
                return self.getTypedRuleContext(CsvParser.CellContext,i)


        def NEWLINE(self):
            return self.getToken(CsvParser.NEWLINE, 0)

        def getRuleIndex(self):
            return CsvParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = CsvParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 16
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 15
                        self.cell()


                    self.state = 18
                    self.match(CsvParser.SEPARATOR)

                else:
                    raise NoViableAltException(self)
                self.state = 21 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 23
                self.cell()


            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CsvParser.NEWLINE:
                self.state = 26
                self.match(CsvParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CellContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CsvParser.WHITESPACE)
            else:
                return self.getToken(CsvParser.WHITESPACE, i)

        def field(self):
            return self.getTypedRuleContext(CsvParser.FieldContext,0)


        def getRuleIndex(self):
            return CsvParser.RULE_cell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCell" ):
                listener.enterCell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCell" ):
                listener.exitCell(self)




    def cell(self):

        localctx = CsvParser.CellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 29
                self.match(CsvParser.WHITESPACE)


            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 32
                self.field()


            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 35
                self.match(CsvParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(CsvParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(CsvParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CsvParser.STRING, 0)

        def getRuleIndex(self):
            return CsvParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = CsvParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CsvParser.INTEGER) | (1 << CsvParser.FLOAT) | (1 << CsvParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





