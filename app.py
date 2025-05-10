import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("📊 Smart Sales Analyzer")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Basic Data Preview")
    st.dataframe(df.head())

    # --- الجزء الأول: التحليل الأساسي ---
    if 'Branch' in df.columns and 'Product' in df.columns:
        top_branch = df['Branch'].value_counts().idxmax()
        top_product = df['Product'].value_counts().idxmax()

        st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
        st.success(f"📦 Most Sold Product: **{top_product}**")
    else:
        st.warning("Missing 'Branch' or 'Product' columns in the file.")

    # --- الجزء الثاني: محاكاة شات بوت ---
    st.subheader("🤖 Smart Sales Chat")
    question = st.selectbox("اسأل سؤالك 👇", [
        "ما هو الفرع الأكثر مبيعًا؟",
        "ما هو المنتج الأكثر مبيعًا؟",
        "كم عدد المنتجات الموجودة؟",
        "كم عدد الفروع؟"
    ])

    if 'Branch' in df.columns and 'Product' in df.columns:
        if question == "ما هو الفرع الأكثر مبيعًا؟":
            top_branch = df['Branch'].value_counts().idxmax()
            st.info(f"🏢 الفرع الأكثر مبيعًا هو: **{top_branch}**")

        elif question == "ما هو المنتج الأكثر مبيعًا؟":
            top_product = df['Product'].value_counts().idxmax()
            st.info(f"📦 المنتج الأكثر مبيعًا هو: **{top_product}**")

        elif question == "كم عدد المنتجات الموجودة؟":
            total_products = df['Product'].nunique()
            st.info(f"🔢 عدد المنتجات المختلفة هو: **{total_products}**")

        elif question == "كم عدد الفروع؟":
            total_branches = df['Branch'].nunique()
            st.info(f"🏬 عدد الفروع هو: **{total_branches}**")
    else:
        st.warning("لا يمكن تحليل الأسئلة لأن الأعمدة المطلوبة غير موجودة.")
else:
    st.info("📂 الرجاء رفع ملف CSV لتحليل البيانات.")
