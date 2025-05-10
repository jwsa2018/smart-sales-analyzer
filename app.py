import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("📊 Smart Sales Analyzer")

# رفع الملف
uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')  # لتفادي مشاكل الترميز
    st.success("✅ File uploaded successfully!")

    # عرض البيانات
    st.subheader("🔍 Basic Data Preview")
    st.dataframe(df.head())

    # --- التحليل الأساسي ---
    if 'Branch' in df.columns and 'Product' in df.columns:
        top_branch = df['Branch'].value_counts().idxmax()
        top_product = df['Product'].value_counts().idxmax()

        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")
    else:
        st.warning("Missing 'Branch' or 'Product' columns in the file.")

    # --- شات بوت وهمي ---
    st.subheader("💬 Smart Sales Chat")
    question = st.selectbox("👇 اسأل سؤالك", [
        "ما هو الفرع الأكثر مبيعًا؟",
        "ما هو المنتج الأكثر مبيعًا؟",
        "كيف أزيد المبيعات؟",
        "هل هناك منتجات ضعيفة؟"
    ])

    if 'Branch' in df.columns and 'Product' in df.columns:
        if question == "ما هو الفرع الأكثر مبيعًا؟":
            top_branch = df['Branch'].value_counts().idxmax()
            st.info(f"🔝 الفرع الأكثر مبيعًا هو: **{top_branch}**")

        elif question == "ما هو المنتج الأكثر مبيعًا؟":
            top_product = df['Product'].value_counts().idxmax()
            st.info(f"🛒 المنتج الأكثر مبيعًا هو: **{top_product}**")

        elif question == "كيف أزيد المبيعات؟":
            st.info("📈 روّج أكثر للمنتجات القوية، وقلل المنتجات الضعيفة، وحفّز الفروع الأقل أداء!")

        elif question == "هل هناك منتجات ضعيفة؟":
            low_sellers = df['Product'].value_counts().tail(3).index.tolist()
            st.info(f"🔻 المنتجات الأقل مبيعًا: {', '.join(low_sellers)}")
