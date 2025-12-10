import streamlit as st

st.title("✉️ Email Generator")

df = st.session_state.get("data")

if df is None:
    st.warning("No data loaded")
else:
    user_id = st.selectbox("Select user", df["user_id"].unique())
    user_row = df[df["user_id"] == user_id].iloc[0]

    st.subheader("User behavior")
    st.json(user_row.to_dict())

    if st.button("Generate Email (Qwen3)"):
        st.info("🔜 LLM integration coming next")
