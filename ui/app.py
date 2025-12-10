import streamlit as st
from components.sidebar import render_sidebar
from state.session import init_session

st.set_page_config(
    page_title="Commerce Barrier Analytics",
    layout="wide"
)

def main():
    init_session()
    render_sidebar()

    st.title("Commerce Barrier Analytics")
    st.markdown("""
    **Demo-система анализа барьеров покупки и генерации email-кампаний**  
    Используется ML-классификация + LLM (Qwen3)
    """)

    if st.session_state.get("data") is None:
        st.info("⬅️ Загрузите CSV-файл в панели слева")

if __name__ == "__main__":
    main()