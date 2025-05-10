import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title(" Smart Sales Analyzer")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    # قراءة الملف وتنظيف المبيعات
    df = pd.read_csv(uploaded_file, encoding='latin1')
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df.dropna(subset=['Sales'], inplace=True)

    st.success("✅ File uploaded successfully!")
    
    # عرض البيانات
    st.subheader("🔍 Basic Data Preview")
    st.dataframe(df.head())

    # تحليل أساسي
    if 'Branch' in df.columns and 'Product' in df.columns and 'Sales' in df.columns:
        top_branch = df.groupby('Branch')['Sales'].sum().idxmax()
        top_product = df.groupby('Product')['Sales'].sum().idxmax()

        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")

        # رسم بياني للمنتجات
        st.subheader("📊 Total Sales per Product")
        product_sales = df.groupby('Product')['Sales'].sum().reset_index()
        fig = px.bar(product_sales, x='Product', y='Sales', color='Product', title='📊 Product Sales')
        st.plotly_chart(fig)

        # رسم بياني للفروع
        st.subheader("🏢 Total Sales per Branch")
        branch_sales = df.groupby('Branch')['Sales'].sum().reset_index()
        fig2 = px.bar(branch_sales, x='Branch', y='Sales', color='Branch', title='🏢 Branch Sales')
        st.plotly_chart(fig2)

        # شات وهمي
        st.subheader("💬 Smart Sales Chat")
        question = st.selectbox("👇 اسأل سؤالك", [
            "كيف أزيد المبيعات؟",
            "ما أفضل فرع؟",
            "ما أفضل منتج؟",
            "ما هي المنتجات الضعيفة؟"
        ])

        if question == "كيف أزيد المبيعات؟":
            st.info("📈 روّج للمنتجات القوية، اعمل عروض للضعيفة، وراجع أداء الفروع.")
        elif question == "ما أفضل فرع؟":
            st.info(f"🏢 الفرع الأقوى مبيعًا هو: **{top_branch}**")
        elif question == "ما أفضل منتج؟":
            st.info(f"📦 المنتج الأعلى مبيعًا هو: **{top_product}**")
        elif question == "ما هي المنتجات الضعيفة؟":
            low_product = df.groupby('Product')['Sales'].sum().idxmin()
            st.warning(f"📉 المنتج الأضعف هو: **{low_product}**")
    else:
        st.warning("⚠️ تأكد أن الملف يحتوي على أعمدة: Branch, Product, Sales")
else:
    st.info("📂 الرجاء رفع ملف CSV لتحليل البيانات.")

