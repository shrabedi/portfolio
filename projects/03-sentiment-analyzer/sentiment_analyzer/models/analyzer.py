"""Main sentiment analyzer with multiple models."""

from typing import Dict, List, Optional

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download required NLTK data
try:
    nltk.data.find("vader_lexicon")
except LookupError:
    nltk.download("vader_lexicon")


class SentimentAnalyzer:
    """Sentiment analysis with multiple models."""

    def __init__(self, model: str = "vader"):
        """
        Initialize analyzer.

        Args:
            model: Model to use ('vader', 'textblob', 'distilbert')
        """
        self.model_name = model

        if model == "vader":
            self.model = SentimentIntensityAnalyzer()
        elif model == "textblob":
            self.model = None  # TextBlob doesn't require pre-loading
        else:
            raise ValueError(f"Unknown model: {model}")

    def predict(self, text: str) -> Dict:
        """
        Predict sentiment.

        Args:
            text: Input text to analyze

        Returns:
            Dictionary with sentiment, score, and confidence
        """
        if self.model_name == "vader":
            return self._predict_vader(text)
        elif self.model_name == "textblob":
            return self._predict_textblob(text)

    def _predict_vader(self, text: str) -> Dict:
        """VADER sentiment prediction."""
        scores = self.model.polarity_scores(text)

        if scores["compound"] >= 0.05:
            sentiment = "positive"
        elif scores["compound"] <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return {
            "text": text,
            "sentiment": sentiment,
            "score": scores["compound"],
            "confidence": max(scores["pos"], scores["neu"], scores["neg"]),
            "details": {
                "positive": scores["pos"],
                "neutral": scores["neu"],
                "negative": scores["neg"],
            },
        }

    def _predict_textblob(self, text: str) -> Dict:
        """TextBlob sentiment prediction."""
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return {
            "text": text,
            "sentiment": sentiment,
            "score": polarity,
            "confidence": abs(polarity),
            "subjectivity": subjectivity,
        }

    def batch_predict(self, texts: List[str]) -> List[Dict]:
        """
        Predict sentiment for multiple texts.

        Args:
            texts: List of texts

        Returns:
            List of predictions
        """
        return [self.predict(text) for text in texts]

    def get_summary(self, texts: List[str]) -> Dict:
        """Get sentiment summary for multiple texts."""
        predictions = self.batch_predict(texts)

        positive = sum(1 for p in predictions if p["sentiment"] == "positive")
        negative = sum(1 for p in predictions if p["sentiment"] == "negative")
        neutral = sum(1 for p in predictions if p["sentiment"] == "neutral")

        return {
            "total": len(texts),
            "positive": positive,
            "negative": negative,
            "neutral": neutral,
            "positive_ratio": positive / len(texts) if texts else 0,
            "negative_ratio": negative / len(texts) if texts else 0,
            "sentiment_distribution": {
                "positive": positive,
                "negative": negative,
                "neutral": neutral,
            },
        }
