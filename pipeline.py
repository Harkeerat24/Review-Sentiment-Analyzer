from input_validator import InputValidator
from text_processor import TextProcessor


def analyze_review(text: object, analyzer):
    validator = InputValidator()
    if not validator.validate(text):
        return {
            "success": False,
            "label": None,
            "error_message": validator.get_error(text),
        }

    try:
        prepared_text = TextProcessor().preprocess(text)
        return analyzer.analyze(prepared_text)
    except Exception:
        return {
            "success": False,
            "label": None,
            "error_message": "The review could not be analyzed. Please try again.",
        }
