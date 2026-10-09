class SummaryManager:
    def __init__(self):
        self.reset()

    def update(self, result):
        if result.get("success") is True:
            label = result.get("label")
            if label == "Positive":
                self.positive_count += 1
            elif label == "Neutral":
                self.neutral_count += 1
            elif label == "Negative":
                self.negative_count += 1
            else:
                return self.get_summary()
            self.total_successful += 1
        return self.get_summary()

    def get_summary(self):
        return {
            "total_successful": self.total_successful,
            "positive_count": self.positive_count,
            "neutral_count": self.neutral_count,
            "negative_count": self.negative_count,
        }

    def percentages(self):
        if self.total_successful == 0:
            return {"Positive": 0.0, "Neutral": 0.0, "Negative": 0.0}
        return {
            "Positive": self.positive_count / self.total_successful * 100,
            "Neutral": self.neutral_count / self.total_successful * 100,
            "Negative": self.negative_count / self.total_successful * 100,
        }

    def reset(self):
        self.total_successful = 0
        self.positive_count = 0
        self.neutral_count = 0
        self.negative_count = 0
