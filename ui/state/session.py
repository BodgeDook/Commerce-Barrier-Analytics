import streamlit as st

def init_session():
    defaults = {
        "data": None,
        "predictions": None,
        "model_loaded": False,
        "selected_user": None
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
