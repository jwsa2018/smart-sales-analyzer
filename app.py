import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("🧠 Smart Sales Analyzer")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')
    st.success("✅ File uploaded successfully!")

    st.subheader("📊 Basic Data Preview")
    st.dataframe(df.head())

    # التحليل الأساسي
    if 'Branch' in df.columns and 'Product' in df.columns:
        top_branch = df['Branch'].value_counts().idxmax()
        top_product = df['Product'].value_counts().idxmax()

        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")
    else:
        st.warning("Missing 'Branch' or 'Product' columns in the file.")

    # رسم بياني حسب المنتج
    if 'Product' in df.columns and 'Sales' in df.columns:
        chart = alt.Chart(df).mark_bar().encode(
            x='Product',
            y='sum(Sales)',
            color='Product',
            tooltip=['Product', 'sum(Sales)']
        ).properties(
            width=600,
            height=400,
            title='📊 Total Sales per Product'
        )
        st.altair_chart(chart)

    # رسم بياني حسب الفرع
    if 'Branch' in df.columns and 'Sales' in df.columns:
        branch_chart = alt.Chart(df).mark_bar().encode(
            x='Branch',
            y='sum(Sales)',
            color='Branch',
            tooltip=['Branch', 'sum(Sales)']
        ).properties(
            width=600,
            height=400,
            title='🏢 Total Sales per Branch'
        )
        st.altair_chart(branch_chart)

    # شات المبيعات
    st.subheader("💬 Smart Sales Chat")
    question = st.selectbox("👎 اسأل سؤالك", [
        "كيف أزيد المبيعات؟",
        "ما أفضل المنتجات؟",
        "ما أقل الفروع أداء؟"
    ])

    if question == "كيف أزيد المبيعات؟":
        st.info("📈 ارفع أكثر المنتجات القوية، وقلل المنتجات الضعيفة، وراجع الفروع الأقل أداء!")

    elif question == "ما أفضل المنتجات؟" and 'Product' in df.columns:
        top_product = df['Product'].value_counts().idxmax()
        st.info(f"🏆 المنتج الأفضل مبيعًا هو: **{top_product}**")

    elif question == "ما أقل الفروع أداء؟" and 'Branch' in df.columns:
        worst_branch = df['Branch'].value_counts().idxmin()
        st.info(f"📉 الفرع الأضعف هو: **{worst_branch}**")

else:
    st.warning("📂 يرجى رفع ملف CSV للمتابعة.")

