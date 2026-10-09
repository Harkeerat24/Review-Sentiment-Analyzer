class TextProcessor:
    def normalize_spaces(self, text: str) -> str:
        return " ".join(text.split())

    def preprocess(self, text: str) -> str:
        return self.normalize_spaces(text)
