import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("📊 Smart Sales Analyzer")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Basic Data Preview")
    st.dataframe(df.head())

    # الجزء الأول: التحليل الأساسي
    if 'Branch' in df.columns and 'Product' in df.columns and 'Sales' in df.columns:
        
        top_branch = df.groupby('Branch')['Sales'].sum().idxmax()
        top_product = df.groupby('Product')['Sales'].sum().idxmax()


        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")
    else:
        st.warning("⚠️ Missing 'Branch', 'Product' or 'Sales' columns in the file.")

    # الجزء الثاني: رسم بياني
    st.subheader("📊 Total Sales per Product")
    product_sales = df.groupby('Product')['Sales'].sum().reset_index()
    fig = px.bar(product_sales, x='Product', y='Sales', color='Product', title='Sales by Product')
    st.plotly_chart(fig)

    # الجزء الثالث: محاكاة شات بوت
    st.subheader("💬 Smart Sales Chat")
    question = st.selectbox("👂 اسأل سؤالك", [
        "كيف أزيد المبيعات؟",
        "ما هو المنتج الأقوى؟",
        "أي فرع هو الأضعف؟",
    ])

    if 'Branch' in df.columns and 'Product' in df.columns and 'Sales' in df.columns:
        if question == "كيف أزيد المبيعات؟":
            st.info("✨ إروّج أكثر للمنتجات القوية، وقلل المنتجات الضعيفة، وراقب الفروع الأقل أداء.")
        elif question == "ما هو المنتج الأقوى؟":
            st.info(f"💡 المنتج الأقوى هو: **{top_product}**")
        elif question == "أي فرع هو الأضعف؟":
            worst_branch = df.groupby('Branch')['Sales'].sum().idxmin()
            st.info(f"📉 أضعف فرع هو: **{worst_branch}**")
