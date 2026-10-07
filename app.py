from pathlib import Path

import streamlit as st

from presentation import show_result, show_summary


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
    layout="centered",
)
st.html(Path(__file__).with_name("styles.css"))

for key, value in {
    "review_text": "",
    "result": None,
    "summary": None,
    "message": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.title("Customer Review Sentiment Analyzer", anchor=False)
st.write("Enter a customer review to see whether its sentiment is positive, negative, or neutral.")

with st.container(border=True, key="review_panel"):
    st.subheader("Customer review", anchor=False)
    st.text_area(
        "Enter or paste a customer review",
        key="review_text",
        height=180,
        placeholder="Write your review here…",
        on_change=hide_old_result,
    )
    st.caption("Use English review text. You can replace it and analyze another review.")

    with st.container(horizontal=True):
        analyze_clicked = st.button("Analyze", type="primary")
        st.button("Clear", on_click=clear_review)

    if analyze_clicked:
        if not st.session_state.review_text.strip():
            st.session_state.result = None
            st.session_state.message = "Enter a review before selecting Analyze."
        else:
            st.session_state.result = None
            st.session_state.message = "Analysis is not connected yet. Your review has been kept."

    if st.session_state.message:
        if st.session_state.review_text.strip():
            st.info(st.session_state.message)
        else:
            st.error(st.session_state.message)

if st.session_state.summary is None:
    with st.container(border=True, key="result_panel"):
        show_result(st.session_state.result)
else:
    result_column, summary_column = st.columns(2)
    with result_column:
        with st.container(border=True, key="result_panel"):
            show_result(st.session_state.result)
    with summary_column:
        with st.container(border=True, key="summary_panel"):
            show_summary(st.session_state.summary)

st.caption("Clear removes the current review and result. Reload the page to start a fresh session.")
