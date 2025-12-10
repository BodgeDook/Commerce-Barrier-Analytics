import streamlit as st

st.title("📊 Data Overview")

df = st.session_state.get("data")

if df is None:
    st.warning("No data loaded")
else:
    st.metric("Users", len(df))
    st.metric("Unique products", df["product_name"].nunique())

    st.subheader("Sample data")
    st.dataframe(df.head(20))
