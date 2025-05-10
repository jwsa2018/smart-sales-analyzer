import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Sales Analyzer")

st.title("📊 Smart Sales Analyzer")
st.write("Upload your sales CSV file")

uploaded_file = st.file_uploader("Drag and drop file here", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='latin1')  # ← هنا التعديل
        st.success("File uploaded successfully!")

        st.subheader("📋 Data Preview")
        st.dataframe(df)

        # رسم شريط بياني لأعلى الفروع مبيعاً
        if 'Branch' in df.columns and 'Total' in df.columns:
            st.subheader("🏪 Top Selling Branches")
            branch_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)
            fig, ax = plt.subplots()
            branch_sales.plot(kind='bar', ax=ax)
            ax.set_ylabel("Total Sales")
            ax.set_xlabel("Branch")
            st.pyplot(fig)

        # عرض الأسئلة الممكنة
        st.subheader("💬 You can ask the chatbot:")
        st.markdown("""
        - What is the top selling branch?
        - What is the top selling product?
        - What is the least profit?
        """)

    except Exception as e:
        st.error(f"An error occurred: {e}")
