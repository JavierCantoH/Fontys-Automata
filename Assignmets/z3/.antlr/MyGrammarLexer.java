// Generated from /Users/javiercanto/Desktop/Automata/Assignmets/z3/MyGrammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SEMICOLON=1, GREATER=2, LESS=3, GREATER_EQUAL=4, LESS_EQUAL=5, BOOLEAN_EQUAL=6, 
		AND=7, OR=8, OPENPARENS=9, CLOSINGPARENS=10, DECLAREFUN=11, INT=12, ID=13, 
		NUMBER=14, ASSERTWORD=15, DISTINCT=16, CHECKSATWORD=17, GETMODELWORD=18, 
		WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SEMICOLON", "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL", "BOOLEAN_EQUAL", 
			"AND", "OR", "OPENPARENS", "CLOSINGPARENS", "DECLAREFUN", "INT", "ID", 
			"NUMBER", "ASSERTWORD", "DISTINCT", "CHECKSATWORD", "GETMODELWORD", "WS"
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


	public MyGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyGrammar.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25\u0089\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6"+
		"\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\7\16U\n"+
		"\16\f\16\16\16X\13\16\3\17\6\17[\n\17\r\17\16\17\\\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\24\6\24\u0084\n\24\r\24\16\24\u0085\3\24\3\24\2"+
		"\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25\3\2\6\5\2C\\aac|\7\2//\62;C\\aac|\3\2\62;\5"+
		"\2\13\f\17\17\"\"\2\u008b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3"+
		"\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2"+
		"\2\2\7-\3\2\2\2\t/\3\2\2\2\13\62\3\2\2\2\r\65\3\2\2\2\17\67\3\2\2\2\21"+
		";\3\2\2\2\23>\3\2\2\2\25@\3\2\2\2\27B\3\2\2\2\31N\3\2\2\2\33R\3\2\2\2"+
		"\35Z\3\2\2\2\37^\3\2\2\2!e\3\2\2\2#n\3\2\2\2%x\3\2\2\2\'\u0083\3\2\2\2"+
		")*\7=\2\2*\4\3\2\2\2+,\7@\2\2,\6\3\2\2\2-.\7>\2\2.\b\3\2\2\2/\60\7@\2"+
		"\2\60\61\7?\2\2\61\n\3\2\2\2\62\63\7>\2\2\63\64\7?\2\2\64\f\3\2\2\2\65"+
		"\66\7?\2\2\66\16\3\2\2\2\678\7c\2\289\7p\2\29:\7f\2\2:\20\3\2\2\2;<\7"+
		"q\2\2<=\7t\2\2=\22\3\2\2\2>?\7*\2\2?\24\3\2\2\2@A\7+\2\2A\26\3\2\2\2B"+
		"C\7f\2\2CD\7g\2\2DE\7e\2\2EF\7n\2\2FG\7c\2\2GH\7t\2\2HI\7g\2\2IJ\7/\2"+
		"\2JK\7h\2\2KL\7w\2\2LM\7p\2\2M\30\3\2\2\2NO\7K\2\2OP\7p\2\2PQ\7v\2\2Q"+
		"\32\3\2\2\2RV\t\2\2\2SU\t\3\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2"+
		"\2W\34\3\2\2\2XV\3\2\2\2Y[\t\4\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]"+
		"\3\2\2\2]\36\3\2\2\2^_\7c\2\2_`\7u\2\2`a\7u\2\2ab\7g\2\2bc\7t\2\2cd\7"+
		"v\2\2d \3\2\2\2ef\7f\2\2fg\7k\2\2gh\7u\2\2hi\7v\2\2ij\7k\2\2jk\7p\2\2"+
		"kl\7e\2\2lm\7v\2\2m\"\3\2\2\2no\7e\2\2op\7j\2\2pq\7g\2\2qr\7e\2\2rs\7"+
		"m\2\2st\7/\2\2tu\7u\2\2uv\7c\2\2vw\7v\2\2w$\3\2\2\2xy\7i\2\2yz\7g\2\2"+
		"z{\7v\2\2{|\7/\2\2|}\7o\2\2}~\7q\2\2~\177\7f\2\2\177\u0080\7g\2\2\u0080"+
		"\u0081\7n\2\2\u0081&\3\2\2\2\u0082\u0084\t\5\2\2\u0083\u0082\3\2\2\2\u0084"+
		"\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\3\2"+
		"\2\2\u0087\u0088\b\24\2\2\u0088(\3\2\2\2\6\2V\\\u0085\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}