import streamlit as st


def show_result(result):
    st.html("<h3>Result</h3>")
    if result is None:
        st.write("Your result will appear here.")
        st.caption("Enter a review above, then select Analyze.")
        return

    label = result["label"]
    colors = {"Positive": "positive", "Negative": "negative", "Neutral": "neutral"}
    explanations = {
        "Positive": "The review expresses a mainly favourable opinion.",
        "Negative": "The review expresses a mainly unfavourable opinion.",
        "Neutral": "The review has a balanced tone or no strong opinion.",
    }
    st.html(f'<span class="sentiment-label {colors[label]}">{label}</span>')
    st.write(explanations[label])


def show_summary(summary):
    st.subheader("Session summary", anchor=False)
    st.caption("Successfully analyzed reviews in this session")
    st.metric("Total analyzed", summary["total_successful"])
    columns = st.columns(3)
    for column, label, field in zip(
        columns,
        ("Positive", "Neutral", "Negative"),
        ("positive_count", "neutral_count", "negative_count"),
    ):
        with column:
            st.metric(label, summary[field])
