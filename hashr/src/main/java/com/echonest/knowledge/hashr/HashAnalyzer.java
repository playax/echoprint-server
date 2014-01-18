package com.echonest.knowledge.hashr;

import java.io.Reader;
import java.util.logging.Logger;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.Tokenizer;
import org.apache.lucene.analysis.core.WhitespaceTokenizer;
import org.apache.lucene.analysis.standard.StandardTokenizer;
import org.apache.lucene.util.Version;

/**
 * An analyzer for a fingerprint hash field that has the form:
 *
 * <pre>
 * <hash> <offset> <hash> <offset>...
 * </pre>
 */
public class HashAnalyzer extends Analyzer {

    protected final static Logger logger = Logger.getLogger(
            HashAnalyzer.class.getName());

	private final Version matchVersion;

	public HashAnalyzer(Version matchVersion) {
		this.matchVersion = matchVersion;
	}

	@Override
	protected TokenStreamComponents createComponents(String fieldName, Reader reader) {
		final Tokenizer source = new StandardTokenizer(matchVersion, reader);
		TokenStream result = new HashFilter(new WhitespaceTokenizer(matchVersion, reader));
		return new TokenStreamComponents(source, result);
	}

}
