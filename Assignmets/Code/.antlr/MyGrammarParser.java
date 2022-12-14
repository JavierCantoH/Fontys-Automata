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
		RETURN=1, COMMA=2, TYPE=3, SEMICOLON=4, GREATER=5, LESS=6, GREATER_EQUAL=7, 
		LESS_EQUAL=8, BOOLEAN_EQUAL=9, BOOLEAN_NOT_EQUAL=10, TEXT=11, WHILE=12, 
		DO=13, AND=14, OR=15, IF=16, THEN=17, ELSE=18, PRINT=19, EQUAL=20, INT=21, 
		FLOAT=22, NEWLINE=23, ID=24, MUL=25, DIV=26, PLUS=27, MIN=28, OPENPARENS=29, 
		CLOSINGPARENS=30, OPENCURLYB=31, CLOSINGCURLYB=32, OPENSQUAREB=33, CLOSINGSQUAREB=34, 
		WS=35;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_expr = 2, RULE_functionDecl = 3, 
		RULE_block = 4, RULE_formalParameters = 5, RULE_formalParameter = 6, RULE_exprList = 7, 
		RULE_print = 8, RULE_loop = 9, RULE_ifStat = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "expr", "functionDecl", "block", "formalParameters", 
			"formalParameter", "exprList", "print", "loop", "ifStat"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'return'", "','", null, "';'", "'>'", "'<'", "'>='", "'<='", "'=='", 
			"'!='", null, "'while'", "'do'", "'and'", "'or'", "'if'", "'then'", "'else'", 
			"'print'", "'='", null, null, null, null, "'*'", "'/'", "'+'", "'-'", 
			"'('", "')'", "'{'", "'}'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "RETURN", "COMMA", "TYPE", "SEMICOLON", "GREATER", "LESS", "GREATER_EQUAL", 
			"LESS_EQUAL", "BOOLEAN_EQUAL", "BOOLEAN_NOT_EQUAL", "TEXT", "WHILE", 
			"DO", "AND", "OR", "IF", "THEN", "ELSE", "PRINT", "EQUAL", "INT", "FLOAT", 
			"NEWLINE", "ID", "MUL", "DIV", "PLUS", "MIN", "OPENPARENS", "CLOSINGPARENS", 
			"OPENCURLYB", "CLOSINGCURLYB", "OPENSQUAREB", "CLOSINGSQUAREB", "WS"
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
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << TYPE) | (1L << TEXT) | (1L << WHILE) | (1L << IF) | (1L << PRINT) | (1L << INT) | (1L << FLOAT) | (1L << NEWLINE) | (1L << ID) | (1L << OPENPARENS))) != 0)) {
				{
				{
				setState(22);
				statement();
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class ReturnFuncContext extends StatementContext {
		public TerminalNode RETURN() { return getToken(MyGrammarParser.RETURN, 0); }
		public TerminalNode SEMICOLON() { return getToken(MyGrammarParser.SEMICOLON, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnFuncContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfExprContext extends StatementContext {
		public IfStatContext ifStat() {
			return getRuleContext(IfStatContext.class,0);
		}
		public IfExprContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class CallingFuncContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MyGrammarParser.SEMICOLON, 0); }
		public CallingFuncContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class FunctionDeclarationContext extends StatementContext {
		public FunctionDeclContext functionDecl() {
			return getRuleContext(FunctionDeclContext.class,0);
		}
		public FunctionDeclarationContext(StatementContext ctx) { copyFrom(ctx); }
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
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				_localctx = new FunctionDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				functionDecl();
				}
				break;
			case 2:
				_localctx = new ReturnFuncContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				match(RETURN);
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << INT) | (1L << FLOAT) | (1L << ID) | (1L << OPENPARENS))) != 0)) {
					{
					setState(30);
					expr(0);
					}
				}

				setState(33);
				match(SEMICOLON);
				}
				break;
			case 3:
				_localctx = new CallingFuncContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(34);
				expr(0);
				setState(35);
				match(SEMICOLON);
				}
				break;
			case 4:
				_localctx = new PrintLineContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(37);
				expr(0);
				setState(38);
				match(NEWLINE);
				}
				break;
			case 5:
				_localctx = new AssignContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(40);
				match(TYPE);
				setState(41);
				match(ID);
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EQUAL) {
					{
					setState(42);
					match(EQUAL);
					setState(43);
					expr(0);
					}
				}

				setState(46);
				match(SEMICOLON);
				}
				break;
			case 6:
				_localctx = new AssignExprContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(47);
				match(ID);
				setState(48);
				match(EQUAL);
				setState(49);
				expr(0);
				setState(50);
				match(SEMICOLON);
				}
				break;
			case 7:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(52);
				match(NEWLINE);
				}
				break;
			case 8:
				_localctx = new PrintExprContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(53);
				print();
				}
				break;
			case 9:
				_localctx = new IfExprContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(54);
				ifStat();
				}
				break;
			case 10:
				_localctx = new LoopExprContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(55);
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
	public static class ExprFuncCallContext extends ExprContext {
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public TerminalNode OPENPARENS() { return getToken(MyGrammarParser.OPENPARENS, 0); }
		public TerminalNode CLOSINGPARENS() { return getToken(MyGrammarParser.CLOSINGPARENS, 0); }
		public ExprListContext exprList() {
			return getRuleContext(ExprListContext.class,0);
		}
		public ExprFuncCallContext(ExprContext ctx) { copyFrom(ctx); }
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
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				_localctx = new ExprFuncCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(59);
				match(ID);
				setState(60);
				match(OPENPARENS);
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << INT) | (1L << FLOAT) | (1L << ID) | (1L << OPENPARENS))) != 0)) {
					{
					setState(61);
					exprList();
					}
				}

				setState(64);
				match(CLOSINGPARENS);
				}
				break;
			case 2:
				{
				_localctx = new NumberContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(65);
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
			case 3:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(66);
				match(ID);
				}
				break;
			case 4:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(67);
				match(OPENPARENS);
				setState(68);
				expr(0);
				setState(69);
				match(CLOSINGPARENS);
				}
				break;
			case 5:
				{
				_localctx = new TextContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(71);
				match(TEXT);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(94);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(92);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(74);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(75);
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
						setState(76);
						((OperationContext)_localctx).right = expr(11);
						}
						break;
					case 2:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(77);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(78);
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
						setState(79);
						((OperationContext)_localctx).right = expr(10);
						}
						break;
					case 3:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(80);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(81);
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
						setState(82);
						((OperationContext)_localctx).right = expr(9);
						}
						break;
					case 4:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(83);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(84);
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
						setState(85);
						((OperationContext)_localctx).right = expr(8);
						}
						break;
					case 5:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(86);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(87);
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
						setState(88);
						((OperationContext)_localctx).right = expr(7);
						}
						break;
					case 6:
						{
						_localctx = new OperationContext(new ExprContext(_parentctx, _parentState));
						((OperationContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(89);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(90);
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
						setState(91);
						((OperationContext)_localctx).right = expr(6);
						}
						break;
					}
					} 
				}
				setState(96);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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

	public static class FunctionDeclContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(MyGrammarParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public TerminalNode OPENPARENS() { return getToken(MyGrammarParser.OPENPARENS, 0); }
		public TerminalNode CLOSINGPARENS() { return getToken(MyGrammarParser.CLOSINGPARENS, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FormalParametersContext formalParameters() {
			return getRuleContext(FormalParametersContext.class,0);
		}
		public FunctionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDecl; }
	}

	public final FunctionDeclContext functionDecl() throws RecognitionException {
		FunctionDeclContext _localctx = new FunctionDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_functionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(TYPE);
			setState(98);
			match(ID);
			setState(99);
			match(OPENPARENS);
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TYPE) {
				{
				setState(100);
				formalParameters();
				}
			}

			setState(103);
			match(CLOSINGPARENS);
			setState(104);
			block();
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

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode OPENCURLYB() { return getToken(MyGrammarParser.OPENCURLYB, 0); }
		public TerminalNode CLOSINGCURLYB() { return getToken(MyGrammarParser.CLOSINGCURLYB, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(OPENCURLYB);
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << TYPE) | (1L << TEXT) | (1L << WHILE) | (1L << IF) | (1L << PRINT) | (1L << INT) | (1L << FLOAT) | (1L << NEWLINE) | (1L << ID) | (1L << OPENPARENS))) != 0)) {
				{
				{
				setState(107);
				statement();
				}
				}
				setState(112);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(113);
			match(CLOSINGCURLYB);
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

	public static class FormalParametersContext extends ParserRuleContext {
		public List<FormalParameterContext> formalParameter() {
			return getRuleContexts(FormalParameterContext.class);
		}
		public FormalParameterContext formalParameter(int i) {
			return getRuleContext(FormalParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MyGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MyGrammarParser.COMMA, i);
		}
		public FormalParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formalParameters; }
	}

	public final FormalParametersContext formalParameters() throws RecognitionException {
		FormalParametersContext _localctx = new FormalParametersContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_formalParameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			formalParameter();
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(116);
				match(COMMA);
				setState(117);
				formalParameter();
				}
				}
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class FormalParameterContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(MyGrammarParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public FormalParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formalParameter; }
	}

	public final FormalParameterContext formalParameter() throws RecognitionException {
		FormalParameterContext _localctx = new FormalParameterContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_formalParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(TYPE);
			setState(124);
			match(ID);
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

	public static class ExprListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MyGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MyGrammarParser.COMMA, i);
		}
		public ExprListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprList; }
	}

	public final ExprListContext exprList() throws RecognitionException {
		ExprListContext _localctx = new ExprListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_exprList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			expr(0);
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(127);
				match(COMMA);
				setState(128);
				expr(0);
				}
				}
				setState(133);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
		enterRule(_localctx, 16, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(PRINT);
			setState(135);
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
		enterRule(_localctx, 18, RULE_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(WHILE);
			setState(138);
			expr(0);
			setState(139);
			match(DO);
			setState(140);
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
		enterRule(_localctx, 20, RULE_ifStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			match(IF);
			setState(143);
			expr(0);
			setState(144);
			match(THEN);
			setState(145);
			statement();
			setState(148);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(146);
				match(ELSE);
				setState(147);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%\u0099\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\3\2\7\2\32\n\2\f\2\16\2\35\13\2\3\3\3\3\3\3\5\3\"\n\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3/\n\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\5\3;\n\3\3\4\3\4\3\4\3\4\5\4A\n\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\5\4K\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4_\n\4\f\4\16\4b\13\4\3\5\3\5\3\5\3\5\5"+
		"\5h\n\5\3\5\3\5\3\5\3\6\3\6\7\6o\n\6\f\6\16\6r\13\6\3\6\3\6\3\7\3\7\3"+
		"\7\7\7y\n\7\f\7\16\7|\13\7\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u0084\n\t\f\t\16"+
		"\t\u0087\13\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\5\f\u0097\n\f\3\f\2\3\6\r\2\4\6\b\n\f\16\20\22\24\26\2\t\3\2\27\30"+
		"\3\2\33\34\3\2\35\36\3\2\20\21\3\2\7\b\3\2\t\n\3\2\13\f\2\u00a9\2\33\3"+
		"\2\2\2\4:\3\2\2\2\6J\3\2\2\2\bc\3\2\2\2\nl\3\2\2\2\fu\3\2\2\2\16}\3\2"+
		"\2\2\20\u0080\3\2\2\2\22\u0088\3\2\2\2\24\u008b\3\2\2\2\26\u0090\3\2\2"+
		"\2\30\32\5\4\3\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2"+
		"\2\34\3\3\2\2\2\35\33\3\2\2\2\36;\5\b\5\2\37!\7\3\2\2 \"\5\6\4\2! \3\2"+
		"\2\2!\"\3\2\2\2\"#\3\2\2\2#;\7\6\2\2$%\5\6\4\2%&\7\6\2\2&;\3\2\2\2\'("+
		"\5\6\4\2()\7\31\2\2);\3\2\2\2*+\7\5\2\2+.\7\32\2\2,-\7\26\2\2-/\5\6\4"+
		"\2.,\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60;\7\6\2\2\61\62\7\32\2\2\62\63\7"+
		"\26\2\2\63\64\5\6\4\2\64\65\7\6\2\2\65;\3\2\2\2\66;\7\31\2\2\67;\5\22"+
		"\n\28;\5\26\f\29;\5\24\13\2:\36\3\2\2\2:\37\3\2\2\2:$\3\2\2\2:\'\3\2\2"+
		"\2:*\3\2\2\2:\61\3\2\2\2:\66\3\2\2\2:\67\3\2\2\2:8\3\2\2\2:9\3\2\2\2;"+
		"\5\3\2\2\2<=\b\4\1\2=>\7\32\2\2>@\7\37\2\2?A\5\20\t\2@?\3\2\2\2@A\3\2"+
		"\2\2AB\3\2\2\2BK\7 \2\2CK\t\2\2\2DK\7\32\2\2EF\7\37\2\2FG\5\6\4\2GH\7"+
		" \2\2HK\3\2\2\2IK\7\r\2\2J<\3\2\2\2JC\3\2\2\2JD\3\2\2\2JE\3\2\2\2JI\3"+
		"\2\2\2K`\3\2\2\2LM\f\f\2\2MN\t\3\2\2N_\5\6\4\rOP\f\13\2\2PQ\t\4\2\2Q_"+
		"\5\6\4\fRS\f\n\2\2ST\t\5\2\2T_\5\6\4\13UV\f\t\2\2VW\t\6\2\2W_\5\6\4\n"+
		"XY\f\b\2\2YZ\t\7\2\2Z_\5\6\4\t[\\\f\7\2\2\\]\t\b\2\2]_\5\6\4\b^L\3\2\2"+
		"\2^O\3\2\2\2^R\3\2\2\2^U\3\2\2\2^X\3\2\2\2^[\3\2\2\2_b\3\2\2\2`^\3\2\2"+
		"\2`a\3\2\2\2a\7\3\2\2\2b`\3\2\2\2cd\7\5\2\2de\7\32\2\2eg\7\37\2\2fh\5"+
		"\f\7\2gf\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7 \2\2jk\5\n\6\2k\t\3\2\2\2lp\7"+
		"!\2\2mo\5\4\3\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qs\3\2\2\2rp\3"+
		"\2\2\2st\7\"\2\2t\13\3\2\2\2uz\5\16\b\2vw\7\4\2\2wy\5\16\b\2xv\3\2\2\2"+
		"y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\r\3\2\2\2|z\3\2\2\2}~\7\5\2\2~\177\7\32"+
		"\2\2\177\17\3\2\2\2\u0080\u0085\5\6\4\2\u0081\u0082\7\4\2\2\u0082\u0084"+
		"\5\6\4\2\u0083\u0081\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085"+
		"\u0086\3\2\2\2\u0086\21\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\7\25\2"+
		"\2\u0089\u008a\5\6\4\2\u008a\23\3\2\2\2\u008b\u008c\7\16\2\2\u008c\u008d"+
		"\5\6\4\2\u008d\u008e\7\17\2\2\u008e\u008f\5\4\3\2\u008f\25\3\2\2\2\u0090"+
		"\u0091\7\22\2\2\u0091\u0092\5\6\4\2\u0092\u0093\7\23\2\2\u0093\u0096\5"+
		"\4\3\2\u0094\u0095\7\24\2\2\u0095\u0097\5\4\3\2\u0096\u0094\3\2\2\2\u0096"+
		"\u0097\3\2\2\2\u0097\27\3\2\2\2\17\33!.:@J^`gpz\u0085\u0096";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}