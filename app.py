from pathlib import Path

import streamlit as st

from presentation import show_result, show_summary
from pipeline import analyze_review
from sentiment_analyzer import SentimentAnalyzer
from summary_manager import SummaryManager


def clear_review():
    st.session_state.review_text = ""
    st.session_state.result = None
    st.session_state.message = ""


def hide_old_result():
    st.session_state.result = None
    st.session_state.message = ""


st.set_page_config(
    page_title="Customer Review Sentiment Analyzer",
    page_icon=":material/sentiment_satisfied:",
    layout="wide",
)
st.html(Path(__file__).with_name("styles.css"))

for key, value in {
    "review_text": "",
    "result": None,
    "message": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

if "analyzer" not in st.session_state:
    st.session_state.analyzer = SentimentAnalyzer()
if "summary_manager" not in st.session_state:
    st.session_state.summary_manager = SummaryManager()

st.title("Customer Review Sentiment Analyzer", anchor=False)
st.write("Analyze English customer reviews.")

review_column, output_column = st.columns(2, gap="small")

with review_column, st.container(border=True, height="stretch", key="review_panel"):
    st.subheader("Customer review", anchor=False)
    st.text_area(
        "Enter or paste a customer review",
        key="review_text",
        height=180,
        placeholder="Write your review here…",
        label_visibility="collapsed",
        on_change=hide_old_result,
    )

    with st.container(horizontal=True):
        analyze_clicked = st.button("Analyze", type="primary")
        st.button("Clear", on_click=clear_review)

    if analyze_clicked:
        st.session_state.result = None
        st.session_state.message = ""
        outcome = analyze_review(
            st.session_state.review_text, st.session_state.analyzer
        )
        if outcome["success"]:
            st.session_state.result = outcome
            st.session_state.summary_manager.update(outcome)
        else:
            st.session_state.message = outcome["error_message"]

    if st.session_state.message:
        st.error(st.session_state.message)

with output_column, st.container(border=True, height="stretch", key="output_panel"):
    with st.container(key="result_panel"):
        show_result(st.session_state.result)
    with st.container(key="summary_panel"):
        show_summary(st.session_state.summary_manager.get_summary())
