import streamlit as st
import pandas as pd

st.title("📊 Smart Sales Analyzer")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    if 'Branch' in df.columns and 'Product' in df.columns:
        top_branch = df['Branch'].value_counts().idxmax()
        top_product = df['Product'].value_counts().idxmax()

        st.success(f"🏢 The top-selling branch is: **{top_branch}**")
        st.success(f"📦 The most sold product is: **{top_product}**")
    else:
        st.error("Make sure your file includes 'Branch' and 'Product' columns.")
