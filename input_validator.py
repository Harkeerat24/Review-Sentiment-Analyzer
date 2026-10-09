class InputValidator:
    def validate(self, text: object) -> bool:
        return self.get_error(text) == ""

    def get_error(self, text: object) -> str:
        if not isinstance(text, str):
            return "Enter the review as text."

        if not text.strip():
            return "Enter a review before selecting Analyze."

        return ""
