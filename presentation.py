import streamlit as st


def show_result(result):
    st.subheader("Result", anchor=False)
    if result is None:
        st.markdown(":gray[—]")
        return

    label = result["label"]
    colors = {"Positive": "green", "Negative": "red", "Neutral": "blue"}
    st.markdown(f":{colors[label]}-background[:{colors[label]}[**{label}**]]")


def show_summary(summary):
    st.subheader("Session summary", anchor=False)
    st.write(f"**Total analyzed: {summary['total_successful']}**")
    with st.container(horizontal=True, horizontal_alignment="distribute", gap="xsmall"):
        for label, field in zip(
            ("Positive", "Neutral", "Negative"),
            ("positive_count", "neutral_count", "negative_count"),
        ):
            st.metric(label, summary[field], width="content")
