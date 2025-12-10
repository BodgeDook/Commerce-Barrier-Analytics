import streamlit as st
import random

st.title("📈 Campaign Simulation")

df = st.session_state.get("data")

if df is None:
    st.warning("No data loaded")
else:
    emails = len(df)
    open_rate = round(random.uniform(0.25, 0.45), 2)
    ctr = round(random.uniform(0.05, 0.15), 2)

    st.metric("Emails sent", emails)
    st.metric("Open rate", open_rate)
    st.metric("Click-through rate", ctr)
