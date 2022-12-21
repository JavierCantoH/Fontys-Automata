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
		TYPE=1, SEMICOLON=2, GREATER=3, LESS=4, GREATER_EQUAL=5, LESS_EQUAL=6, 
		BOOLEAN_EQUAL=7, BOOLEAN_NOT_EQUAL=8, TEXT=9, WHILE=10, DO=11, AND=12, 
		OR=13, IF=14, THEN=15, ELSE=16, PRINT=17, EQUAL=18, INT=19, FLOAT=20, 
		NEWLINE=21, ID=22, MUL=23, DIV=24, PLUS=25, MIN=26, OPENPARENS=27, CLOSINGPARENS=28, 
		WS=29;
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
			null, null, "';'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", null, 
			"'while'", "'do'", "'and'", "'or'", "'if'", "'then'", "'else'", "'print'", 
			"'='", null, null, null, null, "'*'", "'/'", "'+'", "'-'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "TYPE", "SEMICOLON", "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL", 
			"BOOLEAN_EQUAL", "BOOLEAN_NOT_EQUAL", "TEXT", "WHILE", "DO", "AND", "OR", 
			"IF", "THEN", "ELSE", "PRINT", "EQUAL", "INT", "FLOAT", "NEWLINE", "ID", 
			"MUL", "DIV", "PLUS", "MIN", "OPENPARENS", "CLOSINGPARENS", "WS"
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
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TYPE) | (1L << TEXT) | (1L << WHILE) | (1L << IF) | (1L << PRINT) | (1L << INT) | (1L << FLOAT) | (1L << NEWLINE) | (1L << ID) | (1L << OPENPARENS))) != 0) );
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
	public static class AssignExprContext extends StatementContext {
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(MyGrammarParser.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MyGrammarParser.SEMICOLON, 0); }
		public AssignExprContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class AssignContext extends StatementContext {
		public TerminalNode TYPE() { return getToken(MyGrammarParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(MyGrammarParser.SEMICOLON, 0); }
		public TerminalNode EQUAL() { return getToken(MyGrammarParser.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
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
		int _la;
		try {
			setState(36);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
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
				match(TYPE);
				setState(21);
				match(ID);
				setState(24);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EQUAL) {
					{
					setState(22);
					match(EQUAL);
					setState(23);
					expr(0);
					}
				}

				setState(26);
				match(SEMICOLON);
				}
				break;
			case 3:
				_localctx = new AssignExprContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(27);
				match(ID);
				setState(28);
				match(EQUAL);
				setState(29);
				expr(0);
				setState(30);
				match(SEMICOLON);
				}
				break;
			case 4:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(32);
				match(NEWLINE);
				}
				break;
			case 5:
				_localctx = new PrintExprContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(33);
				print();
				}
				break;
			case 6:
				_localctx = new IfExprContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(34);
				ifStat();
				}
				break;
			case 7:
				_localctx = new LoopExprContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(35);
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
	public static class NumberContext extends ExprContext {
		public TerminalNode INT() { return getToken(MyGrammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(MyGrammarParser.FLOAT, 0); }
		public NumberContext(ExprContext ctx) { copyFrom(ctx); }
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
		public TerminalNode GREATER() { return getToken(MyGrammarParser.GREATER, 0); }
		public TerminalNode LESS() { return getToken(MyGrammarParser.LESS, 0); }
		public TerminalNode GREATER_EQUAL() { return getToken(MyGrammarParser.GREATER_EQUAL, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(MyGrammarParser.LESS_EQUAL, 0); }
		public TerminalNode BOOLEAN_EQUAL() { return getToken(MyGrammarParser.BOOLEAN_EQUAL, 0); }
		public TerminalNode BOOLEAN_NOT_EQUAL() { return getToken(MyGrammarParser.BOOLEAN_NOT_EQUAL, 0); }
		public OperationContext(ExprContext ctx) { copyFrom(ctx); }
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
			setState(46);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
				{
				_localctx = new NumberContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(39);
				_la = _input.LA(1);
				if ( !(_la==INT || _la==FLOAT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case ID:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(40);
				match(ID);
				}
				break;
			case OPENPARENS:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(41);
				match(OPENPARENS);
				setState(42);
				expr(0);
				setState(43);
				match(CLOSINGPARENS);
				}
				break;
			case TEXT:
				{
				_localctx = new TextContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(45);
				match(TEXT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(68);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(66);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(48);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(49);
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
						setState(50);
						((OperationContext)_localctx).right = expr(11);
						}
						break;
					case 2:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(51);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(52);
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
						setState(53);
						((OperationContext)_localctx).right = expr(10);
						}
						break;
					case 3:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(54);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(55);
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
						setState(56);
						((OperationContext)_localctx).right = expr(9);
						}
						break;
					case 4:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(57);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(58);
						((OperationContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==GREATER || _la==LESS) ) {
							((OperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(59);
						((OperationContext)_localctx).right = expr(8);
						}
						break;
					case 5:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(60);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(61);
						((OperationContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==GREATER_EQUAL || _la==LESS_EQUAL) ) {
							((OperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(62);
						((OperationContext)_localctx).right = expr(7);
						}
						break;
					case 6:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(63);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(64);
						((OperationContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==BOOLEAN_EQUAL || _la==BOOLEAN_NOT_EQUAL) ) {
							((OperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(65);
						((OperationContext)_localctx).right = expr(6);
						}
						break;
					}
					} 
				}
				setState(70);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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
			setState(71);
			match(PRINT);
			setState(72);
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
			setState(74);
			match(WHILE);
			setState(75);
			expr(0);
			setState(76);
			match(DO);
			setState(77);
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
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(MyGrammarParser.ELSE, 0); }
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
			setState(79);
			match(IF);
			setState(80);
			expr(0);
			setState(81);
			match(THEN);
			setState(82);
			statement();
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(83);
				match(ELSE);
				setState(84);
				statement();
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
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 7);
		case 4:
			return precpred(_ctx, 6);
		case 5:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37Z\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\6\2\20\n\2\r\2\16\2\21\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\5\3\33\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\5\3\'\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\61\n\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4E\n\4\f"+
		"\4\16\4H\13\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\5\7X\n\7\3\7\2\3\6\b\2\4\6\b\n\f\2\t\3\2\25\26\3\2\31\32\3\2\33\34\3"+
		"\2\16\17\3\2\5\6\3\2\7\b\3\2\t\n\2e\2\17\3\2\2\2\4&\3\2\2\2\6\60\3\2\2"+
		"\2\bI\3\2\2\2\nL\3\2\2\2\fQ\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21"+
		"\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\24\5\6\4\2\24\25"+
		"\7\27\2\2\25\'\3\2\2\2\26\27\7\3\2\2\27\32\7\30\2\2\30\31\7\24\2\2\31"+
		"\33\5\6\4\2\32\30\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34\'\7\4\2\2\35"+
		"\36\7\30\2\2\36\37\7\24\2\2\37 \5\6\4\2 !\7\4\2\2!\'\3\2\2\2\"\'\7\27"+
		"\2\2#\'\5\b\5\2$\'\5\f\7\2%\'\5\n\6\2&\23\3\2\2\2&\26\3\2\2\2&\35\3\2"+
		"\2\2&\"\3\2\2\2&#\3\2\2\2&$\3\2\2\2&%\3\2\2\2\'\5\3\2\2\2()\b\4\1\2)\61"+
		"\t\2\2\2*\61\7\30\2\2+,\7\35\2\2,-\5\6\4\2-.\7\36\2\2.\61\3\2\2\2/\61"+
		"\7\13\2\2\60(\3\2\2\2\60*\3\2\2\2\60+\3\2\2\2\60/\3\2\2\2\61F\3\2\2\2"+
		"\62\63\f\f\2\2\63\64\t\3\2\2\64E\5\6\4\r\65\66\f\13\2\2\66\67\t\4\2\2"+
		"\67E\5\6\4\f89\f\n\2\29:\t\5\2\2:E\5\6\4\13;<\f\t\2\2<=\t\6\2\2=E\5\6"+
		"\4\n>?\f\b\2\2?@\t\7\2\2@E\5\6\4\tAB\f\7\2\2BC\t\b\2\2CE\5\6\4\bD\62\3"+
		"\2\2\2D\65\3\2\2\2D8\3\2\2\2D;\3\2\2\2D>\3\2\2\2DA\3\2\2\2EH\3\2\2\2F"+
		"D\3\2\2\2FG\3\2\2\2G\7\3\2\2\2HF\3\2\2\2IJ\7\23\2\2JK\5\6\4\2K\t\3\2\2"+
		"\2LM\7\f\2\2MN\5\6\4\2NO\7\r\2\2OP\5\4\3\2P\13\3\2\2\2QR\7\20\2\2RS\5"+
		"\6\4\2ST\7\21\2\2TW\5\4\3\2UV\7\22\2\2VX\5\4\3\2WU\3\2\2\2WX\3\2\2\2X"+
		"\r\3\2\2\2\t\21\32&\60DFW";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}