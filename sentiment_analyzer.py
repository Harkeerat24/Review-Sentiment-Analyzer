from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    def __init__(self):
        self.model = None

    def analyze(self, text: str):
        if self.model is None:
            self.model = SentimentIntensityAnalyzer()

        scores = self.model.polarity_scores(text)
        return {
            "success": True,
            "label": self.classify(scores["compound"]),
            "compound_score": scores["compound"],
            "positive_score": scores["pos"],
            "neutral_score": scores["neu"],
            "negative_score": scores["neg"],
            "error_message": "",
        }

    def classify(self, score):
        if score >= 0.05:
            return "Positive"
        if score <= -0.05:
            return "Negative"
        return "Neutral"
