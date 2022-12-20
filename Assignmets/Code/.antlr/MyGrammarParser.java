// Generated from /Users/javiercanto/Desktop/Automata/Assignmets/Code/MyGrammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		TEXT=1, WHILE=2, DO=3, AND=4, OR=5, IF=6, THEN=7, ELSE=8, FI=9, PRINT=10, 
		EQUAL=11, INT=12, NEWLINE=13, ID=14, MUL=15, DIV=16, PLUS=17, MIN=18, 
		OPENPARENS=19, CLOSINGPARENS=20, WS=21;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_expr = 2, RULE_print = 3, RULE_loop = 4, 
		RULE_ifStat = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "expr", "print", "loop", "ifStat"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'while'", "'do'", "'and'", "'or'", "'if'", "'then'", "'else'", 
			"'fi'", "'print'", "'='", null, null, null, "'*'", "'/'", "'+'", "'-'", 
			"'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "TEXT", "WHILE", "DO", "AND", "OR", "IF", "THEN", "ELSE", "FI", 
			"PRINT", "EQUAL", "INT", "NEWLINE", "ID", "MUL", "DIV", "PLUS", "MIN", 
			"OPENPARENS", "CLOSINGPARENS", "WS"
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
	public String getGrammarFileName() { return "MyGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MyGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				statement();
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << WHILE) | (1L << IF) | (1L << PRINT) | (1L << INT) | (1L << NEWLINE) | (1L << ID) | (1L << OPENPARENS))) != 0) );
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

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrintLineContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(MyGrammarParser.NEWLINE, 0); }
		public PrintLineContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class LoopExprContext extends StatementContext {
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public LoopExprContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class BlankContext extends StatementContext {
		public TerminalNode NEWLINE() { return getToken(MyGrammarParser.NEWLINE, 0); }
		public BlankContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfExprContext extends StatementContext {
		public IfStatContext ifStat() {
			return getRuleContext(IfStatContext.class,0);
		}
		public IfExprContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class AssignContext extends StatementContext {
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(MyGrammarParser.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(MyGrammarParser.NEWLINE, 0); }
		public AssignContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class PrintExprContext extends StatementContext {
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public PrintExprContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(29);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new PrintLineContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(17);
				expr(0);
				setState(18);
				match(NEWLINE);
				}
				break;
			case 2:
				_localctx = new AssignContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(20);
				match(ID);
				setState(21);
				match(EQUAL);
				setState(22);
				expr(0);
				setState(23);
				match(NEWLINE);
				}
				break;
			case 3:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				match(NEWLINE);
				}
				break;
			case 4:
				_localctx = new PrintExprContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(26);
				print();
				}
				break;
			case 5:
				_localctx = new IfExprContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(27);
				ifStat();
				}
				break;
			case 6:
				_localctx = new LoopExprContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(28);
				loop();
				}
				break;
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

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ParensContext extends ExprContext {
		public TerminalNode OPENPARENS() { return getToken(MyGrammarParser.OPENPARENS, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSINGPARENS() { return getToken(MyGrammarParser.CLOSINGPARENS, 0); }
		public ParensContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class TextContext extends ExprContext {
		public TerminalNode TEXT() { return getToken(MyGrammarParser.TEXT, 0); }
		public TextContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class OperationContext extends ExprContext {
		public ExprContext left;
		public Token op;
		public ExprContext right;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(MyGrammarParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(MyGrammarParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(MyGrammarParser.PLUS, 0); }
		public TerminalNode MIN() { return getToken(MyGrammarParser.MIN, 0); }
		public TerminalNode AND() { return getToken(MyGrammarParser.AND, 0); }
		public TerminalNode OR() { return getToken(MyGrammarParser.OR, 0); }
		public OperationContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends ExprContext {
		public TerminalNode INT() { return getToken(MyGrammarParser.INT, 0); }
		public IntContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(32);
				match(INT);
				}
				break;
			case ID:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(33);
				match(ID);
				}
				break;
			case OPENPARENS:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(34);
				match(OPENPARENS);
				setState(35);
				expr(0);
				setState(36);
				match(CLOSINGPARENS);
				}
				break;
			case TEXT:
				{
				_localctx = new TextContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(38);
				match(TEXT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(52);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(50);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(41);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(42);
						((OperationContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((OperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(43);
						((OperationContext)_localctx).right = expr(8);
						}
						break;
					case 2:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(44);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(45);
						((OperationContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MIN) ) {
							((OperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(46);
						((OperationContext)_localctx).right = expr(7);
						}
						break;
					case 3:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(47);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(48);
						((OperationContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
							((OperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(49);
						((OperationContext)_localctx).right = expr(6);
						}
						break;
					}
					} 
				}
				setState(54);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PrintContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(MyGrammarParser.PRINT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(PRINT);
			setState(56);
			expr(0);
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

	public static class LoopContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(MyGrammarParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode DO() { return getToken(MyGrammarParser.DO, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(WHILE);
			setState(59);
			expr(0);
			setState(60);
			match(DO);
			setState(61);
			statement();
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

	public static class IfStatContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(MyGrammarParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode THEN() { return getToken(MyGrammarParser.THEN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public IfStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStat; }
	}

	public final IfStatContext ifStat() throws RecognitionException {
		IfStatContext _localctx = new IfStatContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_ifStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(IF);
			setState(64);
			expr(0);
			setState(65);
			match(THEN);
			setState(66);
			statement();
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27G\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\6\2\20\n\2\r\2\16\2\21\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\5\4*\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\65\n\4\f"+
		"\4\16\48\13\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\2\3\6\b\2\4\6\b\n\f\2\5\3\2\21\22\3\2\23\24\3\2\6\7\2L\2\17\3\2\2\2\4"+
		"\37\3\2\2\2\6)\3\2\2\2\b9\3\2\2\2\n<\3\2\2\2\fA\3\2\2\2\16\20\5\4\3\2"+
		"\17\16\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2"+
		"\23\24\5\6\4\2\24\25\7\17\2\2\25 \3\2\2\2\26\27\7\20\2\2\27\30\7\r\2\2"+
		"\30\31\5\6\4\2\31\32\7\17\2\2\32 \3\2\2\2\33 \7\17\2\2\34 \5\b\5\2\35"+
		" \5\f\7\2\36 \5\n\6\2\37\23\3\2\2\2\37\26\3\2\2\2\37\33\3\2\2\2\37\34"+
		"\3\2\2\2\37\35\3\2\2\2\37\36\3\2\2\2 \5\3\2\2\2!\"\b\4\1\2\"*\7\16\2\2"+
		"#*\7\20\2\2$%\7\25\2\2%&\5\6\4\2&\'\7\26\2\2\'*\3\2\2\2(*\7\3\2\2)!\3"+
		"\2\2\2)#\3\2\2\2)$\3\2\2\2)(\3\2\2\2*\66\3\2\2\2+,\f\t\2\2,-\t\2\2\2-"+
		"\65\5\6\4\n./\f\b\2\2/\60\t\3\2\2\60\65\5\6\4\t\61\62\f\7\2\2\62\63\t"+
		"\4\2\2\63\65\5\6\4\b\64+\3\2\2\2\64.\3\2\2\2\64\61\3\2\2\2\658\3\2\2\2"+
		"\66\64\3\2\2\2\66\67\3\2\2\2\67\7\3\2\2\28\66\3\2\2\29:\7\f\2\2:;\5\6"+
		"\4\2;\t\3\2\2\2<=\7\4\2\2=>\5\6\4\2>?\7\5\2\2?@\5\4\3\2@\13\3\2\2\2AB"+
		"\7\b\2\2BC\5\6\4\2CD\7\t\2\2DE\5\4\3\2E\r\3\2\2\2\7\21\37)\64\66";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}