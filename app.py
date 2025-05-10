import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("📊 *Smart Sales Analyzer*")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Basic Data Preview")
    st.dataframe(df.head())

    if 'Branch' in df.columns and 'Product' in df.columns and 'Sales' in df.columns:
        # ✅ نحسب الأعلى مبيعًا حسب مجموع المبيعات
        top_branch = df.groupby('Branch')['Sales'].sum().idxmax()
        top_product = df.groupby('Product')['Sales'].sum().idxmax()

        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")

        # 📊 رسم بياني
        st.subheader("📊 Total Sales per Product")
        fig = px.bar(df.groupby("Product")["Sales"].sum().reset_index(),
                     x="Product", y="Sales", color="Product", text="Sales")
        st.plotly_chart(fig)

        # 🤖 شات بوت بسيط
        st.subheader("💬 Smart Sales Chat")
        question = st.selectbox("👎 اسأل سؤالك", [
            "كيف أزيد المبيعات؟",
            "ما هو أفضل منتج؟",
            "ما هو أسوأ فرع؟"
        ])

        if question == "كيف أزيد المبيعات؟":
            st.info("📈 روّج أكتر للمنتجات القوية، وقلل المنتجات الضعيفة، وحفّز الفروع الأقل أداء.")
        elif question == "ما هو أفضل منتج؟":
            st.info(f"🥇 أفضل منتج حسب المبيعات هو: **{top_product}**.")
        elif question == "ما هو أسوأ فرع؟":
            worst_branch = df.groupby('Branch')['Sales'].sum().idxmin()
            st.info(f"📉 أضعف فرع في المبيعات هو: **{worst_branch}**.")
    else:
        st.warning("⚠️ Please make sure your file includes 'Branch', 'Product', and 'Sales' columns.")
else:
    st.info("📂 Please upload a CSV file to get started.")
