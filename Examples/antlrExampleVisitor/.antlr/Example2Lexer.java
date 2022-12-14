// Generated from /Users/javiercanto/Desktop/Automata/Examples/antlrExampleVisitor/Example2.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Example2Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUMBER=1, PLUS=2, AND=3, COMMA=4, PRINT=5, WHILE=6, IF=7, THEN=8, ELSE=9, 
		FI=10, DO=11, DOT=12, TEXT=13, ID=14, WS=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMBER", "PLUS", "AND", "COMMA", "PRINT", "WHILE", "IF", "THEN", "ELSE", 
			"FI", "DO", "DOT", "TEXT", "ID", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'+'", "'and'", "','", "'print'", "'while'", "'if'", "'then'", 
			"'else'", "'fi'", "'do'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUMBER", "PLUS", "AND", "COMMA", "PRINT", "WHILE", "IF", "THEN", 
			"ELSE", "FI", "DO", "DOT", "TEXT", "ID", "WS"
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


	public Example2Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Example2.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21f\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\6\2#\n\2\r\2\16"+
		"\2$\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\7\16R\n\16\f\16\16\16U\13\16"+
		"\3\16\3\16\3\17\3\17\7\17[\n\17\f\17\16\17^\13\17\3\20\6\20a\n\20\r\20"+
		"\16\20b\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f"+
		"\27\r\31\16\33\17\35\20\37\21\3\2\7\3\2\62;\5\2\f\f\17\17$$\5\2C\\aac"+
		"|\b\2##\60\60\62;C\\aac|\5\2\13\f\17\17\"\"\2i\2\3\3\2\2\2\2\5\3\2\2\2"+
		"\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3"+
		"\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2"+
		"\2\2\35\3\2\2\2\2\37\3\2\2\2\3\"\3\2\2\2\5&\3\2\2\2\7(\3\2\2\2\t,\3\2"+
		"\2\2\13.\3\2\2\2\r\64\3\2\2\2\17:\3\2\2\2\21=\3\2\2\2\23B\3\2\2\2\25G"+
		"\3\2\2\2\27J\3\2\2\2\31M\3\2\2\2\33O\3\2\2\2\35X\3\2\2\2\37`\3\2\2\2!"+
		"#\t\2\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\4\3\2\2\2&\'\7-\2"+
		"\2\'\6\3\2\2\2()\7c\2\2)*\7p\2\2*+\7f\2\2+\b\3\2\2\2,-\7.\2\2-\n\3\2\2"+
		"\2./\7r\2\2/\60\7t\2\2\60\61\7k\2\2\61\62\7p\2\2\62\63\7v\2\2\63\f\3\2"+
		"\2\2\64\65\7y\2\2\65\66\7j\2\2\66\67\7k\2\2\678\7n\2\289\7g\2\29\16\3"+
		"\2\2\2:;\7k\2\2;<\7h\2\2<\20\3\2\2\2=>\7v\2\2>?\7j\2\2?@\7g\2\2@A\7p\2"+
		"\2A\22\3\2\2\2BC\7g\2\2CD\7n\2\2DE\7u\2\2EF\7g\2\2F\24\3\2\2\2GH\7h\2"+
		"\2HI\7k\2\2I\26\3\2\2\2JK\7f\2\2KL\7q\2\2L\30\3\2\2\2MN\7\60\2\2N\32\3"+
		"\2\2\2OS\7$\2\2PR\n\3\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3"+
		"\2\2\2US\3\2\2\2VW\7$\2\2W\34\3\2\2\2X\\\t\4\2\2Y[\t\5\2\2ZY\3\2\2\2["+
		"^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\36\3\2\2\2^\\\3\2\2\2_a\t\6\2\2`_\3\2"+
		"\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2cd\3\2\2\2de\b\20\2\2e \3\2\2\2\7\2"+
		"$S\\b\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}