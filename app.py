import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("📊 Smart Sales Analyzer")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

    st.success("✅ File uploaded successfully!")
    
    st.subheader("🔍 Basic Data Preview")
    st.dataframe(df.head())

    # التحليل الأساسي
    if 'Branch' in df.columns and 'Product' in df.columns and 'Sales' in df.columns:
        top_branch = df.groupby('Branch')['Sales'].sum().idxmax()
        top_product = df.groupby('Product')['Sales'].sum().idxmax()

        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")
    else:
        st.warning("⚠️ File must include 'Branch', 'Product', and 'Sales' columns.")

    # رسم بياني
    if 'Product' in df.columns and 'Sales' in df.columns:
        st.subheader("📊 Total Sales per Product")
        fig = px.bar(df.groupby('Product')['Sales'].sum().reset_index(),
                     x='Product', y='Sales', title='Sales by Product')
        st.plotly_chart(fig)

    # شات بوت بسيط
    st.subheader("💬 Smart Sales Chat")
    question = st.selectbox("👂 اسأل سؤالك", [
        "كيف أزيد المبيعات؟",
        "ما هو المنتج الأكثر ربحاً؟",
        "ما هو الفرع الأقوى؟",
        "ما هي المنتجات الضعيفة؟"
    ])

    if question == "كيف أزيد المبيعات؟":
        st.info("📈 اروج أكثر للمنتجات القوية، وقلل المنتجات الضعيفة، و حفز الفروع الأقل أداء.")
    elif question == "ما هو المنتج الأكثر ربحاً؟":
        st.info(f"🏆 المنتج الأكثر مبيعًا هو: **{top_product}**")
    elif question == "ما هو الفرع الأقوى؟":
        st.info(f"🏬 الفرع الأعلى مبيعًا هو: **{top_branch}**")
    elif question == "ما هي المنتجات الضعيفة؟":
        weakest = df.groupby('Product')['Sales'].sum().idxmin()
        st.info(f"📉 المنتج الأضعف مبيعًا هو: **{weakest}**")
