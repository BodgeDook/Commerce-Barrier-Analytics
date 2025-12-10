import streamlit as st
import pandas as pd

def render_sidebar():
    st.sidebar.header("⚙️ Controls")

    uploaded_file = st.sidebar.file_uploader(
        "Upload synthetic CSV",
        type=["csv"]
    )

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state["data"] = df
        st.sidebar.success("✅ Data loaded")

    st.sidebar.divider()

    st.sidebar.markdown("### Pipeline steps")
    st.sidebar.checkbox("ML Model Loaded", value=True, disabled=True)
    st.sidebar.checkbox("LLM Ready", value=True, disabled=True)
