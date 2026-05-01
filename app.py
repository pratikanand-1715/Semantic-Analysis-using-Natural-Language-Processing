import streamlit as st
from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# UI Title streamlit
st.title("Semantic Analysis using NLP")
st.subheader("Sentiment + Text Summarization System")

# Input
text = st.text_area("Enter your text:")

# Buttons
col1, col2 = st.columns(2)

# SENTIMENT ANALYSIS
with col1:
    if st.button("Analyze Sentiment"):
        if text:
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity

            if polarity > 0:
                st.success("Positive")
            elif polarity < 0:
                st.error("Negative")
            else:
                st.info("Neutral")

            st.write(f"Polarity Score: {polarity}")
        else:
            st.warning("Please enter text")

#  TEXT SUMMARIZATION
with col2:
    if st.button("Summarize Text"):
        if text:
            sentences = sent_tokenize(text)
            words = word_tokenize(text.lower())

            stop_words = set(stopwords.words("english"))
            words = [w for w in words if w.isalnum() and w not in stop_words]

            freq = Counter(words)

            sentence_scores = {}
            for sent in sentences:
                for word in word_tokenize(sent.lower()):
                    if word in freq:
                        if sent not in sentence_scores:
                            sentence_scores[sent] = freq[word]
                        else:
                            sentence_scores[sent] += freq[word]

            summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

            st.success("Summary:")
            for s in summary:
                st.write(s)
        else:
            st.warning("Please enter text")

# Footer
st.markdown("---")
st.write("Developed as NLP Final Year Project")