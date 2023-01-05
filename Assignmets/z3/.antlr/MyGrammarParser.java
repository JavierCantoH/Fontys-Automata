// Generated from /Users/javiercanto/Desktop/Automata/Assignmets/z3/MyGrammar.g4 by ANTLR 4.9.2
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
		SEMICOLON=1, GREATER=2, LESS=3, GREATER_EQUAL=4, LESS_EQUAL=5, BOOLEAN_EQUAL=6, 
		AND=7, OR=8, OPENPARENS=9, CLOSINGPARENS=10, DECLAREFUN=11, INT=12, ID=13, 
		NUMBER=14, ASSERTWORD=15, DISTINCT=16, CHECKSATWORD=17, GETMODELWORD=18, 
		WS=19;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_declaration = 2, RULE_checksat = 3, 
		RULE_getmodel = 4, RULE_assertion = 5, RULE_constraint = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "declaration", "checksat", "getmodel", "assertion", 
			"constraint"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'>'", "'<'", "'>='", "'<='", "'='", "'and'", "'or'", "'('", 
			"')'", "'declare-fun'", "'Int'", null, null, "'assert'", "'distinct'", 
			"'check-sat'", "'get-model'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SEMICOLON", "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL", 
			"BOOLEAN_EQUAL", "AND", "OR", "OPENPARENS", "CLOSINGPARENS", "DECLAREFUN", 
			"INT", "ID", "NUMBER", "ASSERTWORD", "DISTINCT", "CHECKSATWORD", "GETMODELWORD", 
			"WS"
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
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPENPARENS) {
				{
				{
				setState(14);
				statement();
				}
				}
				setState(19);
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
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public ChecksatContext checksat() {
			return getRuleContext(ChecksatContext.class,0);
		}
		public GetmodelContext getmodel() {
			return getRuleContext(GetmodelContext.class,0);
		}
		public AssertionContext assertion() {
			return getRuleContext(AssertionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(24);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(20);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(21);
				checksat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(22);
				getmodel();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(23);
				assertion();
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

	public static class DeclarationContext extends ParserRuleContext {
		public List<TerminalNode> OPENPARENS() { return getTokens(MyGrammarParser.OPENPARENS); }
		public TerminalNode OPENPARENS(int i) {
			return getToken(MyGrammarParser.OPENPARENS, i);
		}
		public TerminalNode DECLAREFUN() { return getToken(MyGrammarParser.DECLAREFUN, 0); }
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public List<TerminalNode> CLOSINGPARENS() { return getTokens(MyGrammarParser.CLOSINGPARENS); }
		public TerminalNode CLOSINGPARENS(int i) {
			return getToken(MyGrammarParser.CLOSINGPARENS, i);
		}
		public TerminalNode INT() { return getToken(MyGrammarParser.INT, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(OPENPARENS);
			setState(27);
			match(DECLAREFUN);
			setState(28);
			match(ID);
			setState(29);
			match(OPENPARENS);
			setState(30);
			match(CLOSINGPARENS);
			setState(31);
			match(INT);
			setState(32);
			match(CLOSINGPARENS);
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

	public static class ChecksatContext extends ParserRuleContext {
		public TerminalNode OPENPARENS() { return getToken(MyGrammarParser.OPENPARENS, 0); }
		public TerminalNode CHECKSATWORD() { return getToken(MyGrammarParser.CHECKSATWORD, 0); }
		public TerminalNode CLOSINGPARENS() { return getToken(MyGrammarParser.CLOSINGPARENS, 0); }
		public ChecksatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_checksat; }
	}

	public final ChecksatContext checksat() throws RecognitionException {
		ChecksatContext _localctx = new ChecksatContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_checksat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(OPENPARENS);
			setState(35);
			match(CHECKSATWORD);
			setState(36);
			match(CLOSINGPARENS);
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

	public static class GetmodelContext extends ParserRuleContext {
		public TerminalNode OPENPARENS() { return getToken(MyGrammarParser.OPENPARENS, 0); }
		public TerminalNode GETMODELWORD() { return getToken(MyGrammarParser.GETMODELWORD, 0); }
		public TerminalNode CLOSINGPARENS() { return getToken(MyGrammarParser.CLOSINGPARENS, 0); }
		public GetmodelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_getmodel; }
	}

	public final GetmodelContext getmodel() throws RecognitionException {
		GetmodelContext _localctx = new GetmodelContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_getmodel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(OPENPARENS);
			setState(39);
			match(GETMODELWORD);
			setState(40);
			match(CLOSINGPARENS);
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

	public static class AssertionContext extends ParserRuleContext {
		public TerminalNode OPENPARENS() { return getToken(MyGrammarParser.OPENPARENS, 0); }
		public TerminalNode ASSERTWORD() { return getToken(MyGrammarParser.ASSERTWORD, 0); }
		public ConstraintContext constraint() {
			return getRuleContext(ConstraintContext.class,0);
		}
		public TerminalNode CLOSINGPARENS() { return getToken(MyGrammarParser.CLOSINGPARENS, 0); }
		public AssertionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertion; }
	}

	public final AssertionContext assertion() throws RecognitionException {
		AssertionContext _localctx = new AssertionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assertion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(OPENPARENS);
			setState(43);
			match(ASSERTWORD);
			setState(44);
			constraint();
			setState(45);
			match(CLOSINGPARENS);
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

	public static class ConstraintContext extends ParserRuleContext {
		public TerminalNode OPENPARENS() { return getToken(MyGrammarParser.OPENPARENS, 0); }
		public TerminalNode DISTINCT() { return getToken(MyGrammarParser.DISTINCT, 0); }
		public TerminalNode CLOSINGPARENS() { return getToken(MyGrammarParser.CLOSINGPARENS, 0); }
		public List<TerminalNode> ID() { return getTokens(MyGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MyGrammarParser.ID, i);
		}
		public TerminalNode AND() { return getToken(MyGrammarParser.AND, 0); }
		public List<ConstraintContext> constraint() {
			return getRuleContexts(ConstraintContext.class);
		}
		public ConstraintContext constraint(int i) {
			return getRuleContext(ConstraintContext.class,i);
		}
		public TerminalNode OR() { return getToken(MyGrammarParser.OR, 0); }
		public TerminalNode GREATER() { return getToken(MyGrammarParser.GREATER, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(MyGrammarParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(MyGrammarParser.NUMBER, i);
		}
		public TerminalNode LESS() { return getToken(MyGrammarParser.LESS, 0); }
		public TerminalNode GREATER_EQUAL() { return getToken(MyGrammarParser.GREATER_EQUAL, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(MyGrammarParser.LESS_EQUAL, 0); }
		public TerminalNode BOOLEAN_EQUAL() { return getToken(MyGrammarParser.BOOLEAN_EQUAL, 0); }
		public ConstraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constraint; }
	}

	public final ConstraintContext constraint() throws RecognitionException {
		ConstraintContext _localctx = new ConstraintContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_constraint);
		int _la;
		try {
			setState(92);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(47);
				match(OPENPARENS);
				setState(48);
				match(DISTINCT);
				setState(50); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(49);
					match(ID);
					}
					}
					setState(52); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ID );
				setState(54);
				match(CLOSINGPARENS);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				match(OPENPARENS);
				setState(56);
				match(AND);
				setState(57);
				constraint();
				setState(58);
				constraint();
				setState(59);
				match(CLOSINGPARENS);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(61);
				match(OPENPARENS);
				setState(62);
				match(OR);
				setState(63);
				constraint();
				setState(64);
				constraint();
				setState(65);
				match(CLOSINGPARENS);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(67);
				match(OPENPARENS);
				setState(68);
				match(GREATER);
				setState(69);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(70);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(71);
				match(CLOSINGPARENS);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(72);
				match(OPENPARENS);
				setState(73);
				match(LESS);
				setState(74);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(75);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(76);
				match(CLOSINGPARENS);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(77);
				match(OPENPARENS);
				setState(78);
				match(GREATER_EQUAL);
				setState(79);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(80);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(81);
				match(CLOSINGPARENS);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(82);
				match(OPENPARENS);
				setState(83);
				match(LESS_EQUAL);
				setState(84);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(85);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(86);
				match(CLOSINGPARENS);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(87);
				match(OPENPARENS);
				setState(88);
				match(BOOLEAN_EQUAL);
				setState(89);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(90);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==NUMBER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(91);
				match(CLOSINGPARENS);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25a\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\7\2\22\n\2\f\2\16\2\25"+
		"\13\2\3\3\3\3\3\3\3\3\5\3\33\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3"+
		"\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\6\b\65\n\b"+
		"\r\b\16\b\66\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\5\b_\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\17"+
		"\20\2e\2\23\3\2\2\2\4\32\3\2\2\2\6\34\3\2\2\2\b$\3\2\2\2\n(\3\2\2\2\f"+
		",\3\2\2\2\16^\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21"+
		"\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\23\3\2\2\2\26\33\5\6\4\2\27\33"+
		"\5\b\5\2\30\33\5\n\6\2\31\33\5\f\7\2\32\26\3\2\2\2\32\27\3\2\2\2\32\30"+
		"\3\2\2\2\32\31\3\2\2\2\33\5\3\2\2\2\34\35\7\13\2\2\35\36\7\r\2\2\36\37"+
		"\7\17\2\2\37 \7\13\2\2 !\7\f\2\2!\"\7\16\2\2\"#\7\f\2\2#\7\3\2\2\2$%\7"+
		"\13\2\2%&\7\23\2\2&\'\7\f\2\2\'\t\3\2\2\2()\7\13\2\2)*\7\24\2\2*+\7\f"+
		"\2\2+\13\3\2\2\2,-\7\13\2\2-.\7\21\2\2./\5\16\b\2/\60\7\f\2\2\60\r\3\2"+
		"\2\2\61\62\7\13\2\2\62\64\7\22\2\2\63\65\7\17\2\2\64\63\3\2\2\2\65\66"+
		"\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\678\3\2\2\28_\7\f\2\29:\7\13\2\2"+
		":;\7\t\2\2;<\5\16\b\2<=\5\16\b\2=>\7\f\2\2>_\3\2\2\2?@\7\13\2\2@A\7\n"+
		"\2\2AB\5\16\b\2BC\5\16\b\2CD\7\f\2\2D_\3\2\2\2EF\7\13\2\2FG\7\4\2\2GH"+
		"\t\2\2\2HI\t\2\2\2I_\7\f\2\2JK\7\13\2\2KL\7\5\2\2LM\t\2\2\2MN\t\2\2\2"+
		"N_\7\f\2\2OP\7\13\2\2PQ\7\6\2\2QR\t\2\2\2RS\t\2\2\2S_\7\f\2\2TU\7\13\2"+
		"\2UV\7\7\2\2VW\t\2\2\2WX\t\2\2\2X_\7\f\2\2YZ\7\13\2\2Z[\7\b\2\2[\\\t\2"+
		"\2\2\\]\t\2\2\2]_\7\f\2\2^\61\3\2\2\2^9\3\2\2\2^?\3\2\2\2^E\3\2\2\2^J"+
		"\3\2\2\2^O\3\2\2\2^T\3\2\2\2^Y\3\2\2\2_\17\3\2\2\2\6\23\32\66^";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}