// Generated from /Users/wes/projects/csv_parser/csv_parser/antlr_generated/Csv.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CsvParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INTEGER=1, FLOAT=2, NEWLINE=3, SEPARATOR=4, WHITESPACE=5;
	public static final int
		RULE_csv = 0, RULE_line = 1, RULE_cell = 2, RULE_field = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"csv", "line", "cell", "field"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INTEGER", "FLOAT", "NEWLINE", "SEPARATOR", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Csv.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CsvParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class CsvContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CsvParser.EOF, 0); }
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public CsvContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_csv; }
	}

	public final CsvContext csv() throws RecognitionException {
		CsvContext _localctx = new CsvContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_csv);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(8);
				line();
				}
				}
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << SEPARATOR) | (1L << WHITESPACE))) != 0) );
			setState(13);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LineContext extends ParserRuleContext {
		public List<TerminalNode> SEPARATOR() { return getTokens(CsvParser.SEPARATOR); }
		public TerminalNode SEPARATOR(int i) {
			return getToken(CsvParser.SEPARATOR, i);
		}
		public List<CellContext> cell() {
			return getRuleContexts(CellContext.class);
		}
		public CellContext cell(int i) {
			return getRuleContext(CellContext.class,i);
		}
		public TerminalNode NEWLINE() { return getToken(CsvParser.NEWLINE, 0); }
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_line);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(19); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(16);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						setState(15);
						cell();
						}
						break;
					}
					setState(18);
					match(SEPARATOR);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(21); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(24);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(23);
				cell();
				}
				break;
			}
			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEWLINE) {
				{
				setState(26);
				match(NEWLINE);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CellContext extends ParserRuleContext {
		public List<TerminalNode> WHITESPACE() { return getTokens(CsvParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(CsvParser.WHITESPACE, i);
		}
		public FieldContext field() {
			return getRuleContext(FieldContext.class,0);
		}
		public CellContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cell; }
	}

	public final CellContext cell() throws RecognitionException {
		CellContext _localctx = new CellContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_cell);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(29);
				match(WHITESPACE);
				}
				break;
			}
			setState(33);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(32);
				field();
				}
				break;
			}
			setState(36);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(35);
				match(WHITESPACE);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FieldContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(CsvParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(CsvParser.FLOAT, 0); }
		public FieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field; }
	}

	public final FieldContext field() throws RecognitionException {
		FieldContext _localctx = new FieldContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_field);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			_la = _input.LA(1);
			if ( !(_la==INTEGER || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7+\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16\2\r\3\2\3\2\3\3\5\3\23\n\3\3\3"+
		"\6\3\26\n\3\r\3\16\3\27\3\3\5\3\33\n\3\3\3\5\3\36\n\3\3\4\5\4!\n\4\3\4"+
		"\5\4$\n\4\3\4\5\4\'\n\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\3\3\2\3\4\2.\2\13"+
		"\3\2\2\2\4\25\3\2\2\2\6 \3\2\2\2\b(\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f"+
		"\r\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3"+
		"\3\2\2\2\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\26"+
		"\7\6\2\2\25\22\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\32"+
		"\3\2\2\2\31\33\5\6\4\2\32\31\3\2\2\2\32\33\3\2\2\2\33\35\3\2\2\2\34\36"+
		"\7\5\2\2\35\34\3\2\2\2\35\36\3\2\2\2\36\5\3\2\2\2\37!\7\7\2\2 \37\3\2"+
		"\2\2 !\3\2\2\2!#\3\2\2\2\"$\5\b\5\2#\"\3\2\2\2#$\3\2\2\2$&\3\2\2\2%\'"+
		"\7\7\2\2&%\3\2\2\2&\'\3\2\2\2\'\7\3\2\2\2()\t\2\2\2)\t\3\2\2\2\n\r\22"+
		"\27\32\35 #&";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}