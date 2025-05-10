import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("📊 Smart Sales Analyzer")

# رفع الملف
uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Basic Data Preview")
    st.dataframe(df.head())

    # الجزء الأول: التحليل الأساسي
    if {'Branch', 'Product', 'Sales'}.issubset(df.columns):
        top_branch = df.groupby('Branch')['Sales'].sum().idxmax()
        top_product = df.groupby('Product')['Sales'].sum().idxmax()

        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")

        # رسم بياني
        st.subheader("📊 Total Sales per Product")
        chart = px.bar(df, x='Product', y='Sales', color='Product', title='Sales by Product', text_auto=True)
        st.plotly_chart(chart)

        # الجزء الثاني: شات ذكي بسيط
        st.subheader("💬 Smart Sales Chat")
        st.write("👂 اسأل سؤالك")

        question = st.selectbox("👇 اختر سؤالاً", [
            "كيف أزيد المبيعات؟",
            "ما هو المنتج الأكثر ربحًا؟",
            "ما هو الفرع الأفضل أداء؟"
        ])

        if question == "كيف أزيد المبيعات؟":
            st.info("📈 روّج أكثر للمنتجات القوية، وقلل المنتجات الضعيفة، وحفز الفروع الأقل أداء.")
        elif question == "ما هو المنتج الأكثر ربحًا؟":
            st.info(f"💰 أكثر منتج مبيعًا هو **{top_product}**.")
        elif question == "ما هو الفرع الأفضل أداء؟":
            st.info(f"🏢 الفرع الأعلى مبيعًا هو **{top_branch}**.")
    else:
        st.warning("❗ تأكد من وجود الأعمدة: 'Branch', 'Product', 'Sales'")
else:
    st.info("📁 الرجاء رفع ملف CSV لبدء التحليل.")
