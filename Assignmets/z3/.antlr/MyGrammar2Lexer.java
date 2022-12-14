// Generated from /Users/javiercanto/Desktop/Automata/Assignmets/z3/MyGrammar2.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyGrammar2Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, COMMENT=17, 
		ID=18, NUMBER=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "COMMENT", 
			"ID", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "'declare-fun'", "'()'", "'Int'", "')'", "'assert'", "'distinct'", 
			"'>='", "'<='", "'<'", "'>'", "'='", "'and'", "'or'", "'check-sat'", 
			"'get-model'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "COMMENT", "ID", "NUMBER", "WS"
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


	public MyGrammar2Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyGrammar2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26\u009b\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3"+
		"\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\7\22|\n\22\f\22\16\22\177\13\22"+
		"\3\22\3\22\3\22\3\22\3\23\6\23\u0086\n\23\r\23\16\23\u0087\3\23\7\23\u008b"+
		"\n\23\f\23\16\23\u008e\13\23\3\24\6\24\u0091\n\24\r\24\16\24\u0092\3\25"+
		"\6\25\u0096\n\25\r\25\16\25\u0097\3\25\3\25\3}\2\26\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'"+
		"\25)\26\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2\u009f"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5-\3\2\2\2\79\3\2\2"+
		"\2\t<\3\2\2\2\13@\3\2\2\2\rB\3\2\2\2\17I\3\2\2\2\21R\3\2\2\2\23U\3\2\2"+
		"\2\25X\3\2\2\2\27Z\3\2\2\2\31\\\3\2\2\2\33^\3\2\2\2\35b\3\2\2\2\37e\3"+
		"\2\2\2!o\3\2\2\2#y\3\2\2\2%\u0085\3\2\2\2\'\u0090\3\2\2\2)\u0095\3\2\2"+
		"\2+,\7*\2\2,\4\3\2\2\2-.\7f\2\2./\7g\2\2/\60\7e\2\2\60\61\7n\2\2\61\62"+
		"\7c\2\2\62\63\7t\2\2\63\64\7g\2\2\64\65\7/\2\2\65\66\7h\2\2\66\67\7w\2"+
		"\2\678\7p\2\28\6\3\2\2\29:\7*\2\2:;\7+\2\2;\b\3\2\2\2<=\7K\2\2=>\7p\2"+
		"\2>?\7v\2\2?\n\3\2\2\2@A\7+\2\2A\f\3\2\2\2BC\7c\2\2CD\7u\2\2DE\7u\2\2"+
		"EF\7g\2\2FG\7t\2\2GH\7v\2\2H\16\3\2\2\2IJ\7f\2\2JK\7k\2\2KL\7u\2\2LM\7"+
		"v\2\2MN\7k\2\2NO\7p\2\2OP\7e\2\2PQ\7v\2\2Q\20\3\2\2\2RS\7@\2\2ST\7?\2"+
		"\2T\22\3\2\2\2UV\7>\2\2VW\7?\2\2W\24\3\2\2\2XY\7>\2\2Y\26\3\2\2\2Z[\7"+
		"@\2\2[\30\3\2\2\2\\]\7?\2\2]\32\3\2\2\2^_\7c\2\2_`\7p\2\2`a\7f\2\2a\34"+
		"\3\2\2\2bc\7q\2\2cd\7t\2\2d\36\3\2\2\2ef\7e\2\2fg\7j\2\2gh\7g\2\2hi\7"+
		"e\2\2ij\7m\2\2jk\7/\2\2kl\7u\2\2lm\7c\2\2mn\7v\2\2n \3\2\2\2op\7i\2\2"+
		"pq\7g\2\2qr\7v\2\2rs\7/\2\2st\7o\2\2tu\7q\2\2uv\7f\2\2vw\7g\2\2wx\7n\2"+
		"\2x\"\3\2\2\2y}\7=\2\2z|\13\2\2\2{z\3\2\2\2|\177\3\2\2\2}~\3\2\2\2}{\3"+
		"\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081\7\f\2\2\u0081\u0082\3\2"+
		"\2\2\u0082\u0083\b\22\2\2\u0083$\3\2\2\2\u0084\u0086\t\2\2\2\u0085\u0084"+
		"\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088"+
		"\u008c\3\2\2\2\u0089\u008b\t\3\2\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2"+
		"\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d&\3\2\2\2\u008e\u008c"+
		"\3\2\2\2\u008f\u0091\t\4\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092"+
		"\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093(\3\2\2\2\u0094\u0096\t\5\2\2"+
		"\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098"+
		"\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b\25\2\2\u009a*\3\2\2\2\b\2}"+
		"\u0087\u008c\u0092\u0097\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}