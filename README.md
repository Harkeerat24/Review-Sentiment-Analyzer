# Customer Review Sentiment Analyzer

A Python application for analyzing the sentiment of English customer reviews. Built with Streamlit and VADER, it classifies each review as **Positive**, **Negative**, or **Neutral** and tracks sentiment counts within the current session.

## Requirements

- Python 3.10 or newer
- Streamlit 1.65.0
- vaderSentiment 3.3.2

## Installation

Clone the repository and open the project folder:

```bash
git clone https://github.com/Harkeerat24/Review-Sentiment-Analyzer.git
cd Review-Sentiment-Analyzer
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux, macOS, or WSL**

```bash
source .venv/bin/activate
```

Create and activate the environment on the same operating system. Use a separate environment for Windows and WSL.

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Start the application:

```bash
python -m streamlit run app.py
```

Open the address shown in the terminal, usually `http://localhost:8501`.

1. Enter or paste a customer review.
2. Select **Analyze** to display its sentiment and update the session summary.
3. Replace the text to analyze another review, or select **Clear** to remove the current input and result.

The summary starts at zero. Each successful analysis counts once, including repeated analysis of the same text. Editing, Clear, validation errors, and analysis failures leave the counts unchanged. Reloading the page starts a new session.

## How it works

```text
Review input → Validation → Text preparation → VADER analysis
                                                   ↓
                                      Result and session summary
```

Validation rejects non-text values and empty or whitespace-only input. Text preparation normalizes whitespace while preserving capitalization, punctuation, negation, and emoticons.

VADER's compound score determines the label:

| Compound score             | Sentiment |
| -------------------------- | --------- |
| `≥ 0.05`                   | Positive  |
| `≤ -0.05`                  | Negative  |
| Between `-0.05` and `0.05` | Neutral   |

The interface displays the label; the analyzer also returns compound and per-class scores. The compound score is not a confidence percentage.

## Project structure

```text
├── app.py                  # Interface and session state
├── input_validator.py      # Input validation
├── text_processor.py       # Whitespace normalization
├── sentiment_analyzer.py   # VADER analysis and classification
├── pipeline.py             # Analysis flow and error handling
├── summary_manager.py      # Session counts and percentages
├── presentation.py         # Result and summary display
├── styles.css              # Responsive layout and styling
├── .streamlit/config.toml  # Streamlit theme and configuration
└── requirements.txt        # Python dependencies
```

## Limitations and data handling

The application is intended for English reviews. It accepts all nonempty text and does not detect language or determine whether a review is meaningful. Sarcasm, specialized vocabulary, and mixed opinions may produce inaccurate classifications.

Review text, results, and counters are held in temporary session memory. The application does not save review history or use a database.
