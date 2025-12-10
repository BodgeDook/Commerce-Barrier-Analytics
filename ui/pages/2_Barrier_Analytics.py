import streamlit as st

st.title("🧠 Barrier Analytics")

df = st.session_state.get("data")

if df is None:
    st.warning("No data loaded")
else:
    if "Barrier_Class" in df.columns:
        counts = df["Barrier_Class"].value_counts().sort_index()
        st.bar_chart(counts)
    else:
        st.info("Barrier predictions not available yet")
