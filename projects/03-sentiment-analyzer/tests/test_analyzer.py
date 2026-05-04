"""Tests for SentimentAnalyzer."""

import pytest

from sentiment_analyzer import SentimentAnalyzer


@pytest.fixture
def vader_analyzer():
    """Create VADER analyzer."""
    return SentimentAnalyzer(model="vader")


@pytest.fixture
def textblob_analyzer():
    """Create TextBlob analyzer."""
    return SentimentAnalyzer(model="textblob")


def test_vader_positive(vader_analyzer):
    """Test VADER positive sentiment."""
    result = vader_analyzer.predict("I absolutely love this product!")
    assert result["sentiment"] == "positive"
    assert result["score"] > 0.5


def test_vader_negative(vader_analyzer):
    """Test VADER negative sentiment."""
    result = vader_analyzer.predict("This is terrible and awful")
    assert result["sentiment"] == "negative"
    assert result["score"] < -0.5


def test_vader_neutral(vader_analyzer):
    """Test VADER neutral sentiment."""
    result = vader_analyzer.predict("The sky is blue")
    assert result["sentiment"] == "neutral"


def test_textblob_positive(textblob_analyzer):
    """Test TextBlob positive sentiment."""
    result = textblob_analyzer.predict("Great job!")
    assert result["sentiment"] == "positive"


def test_batch_predict(vader_analyzer):
    """Test batch prediction."""
    texts = ["I love this!", "This is bad", "It's okay"]
    results = vader_analyzer.batch_predict(texts)
    assert len(results) == 3


def test_summary(vader_analyzer):
    """Test sentiment summary."""
    texts = ["Great!", "Terrible", "Good", "Bad", "Okay"]
    summary = vader_analyzer.get_summary(texts)
    assert summary["total"] == 5
    assert "positive_ratio" in summary
