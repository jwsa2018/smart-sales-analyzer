import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Sales Analyzer", layout="centered")
st.title("📊 Smart Sales Analyzer")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='latin1')
        st.success("✅ File uploaded successfully!")

        st.subheader("🔍 Basic Data Preview")
        st.dataframe(df.head())

        if 'Branch' in df.columns and 'Product' in df.columns:
            # التحليل الأساسي
            top_branch = df['Branch'].value_counts().idxmax()
            top_product = df['Product'].value_counts().idxmax()

            st.success(f"🏢 Top-Selling Branch: **{top_branch}**")
            st.success(f"📦 Most Sold Product: **{top_product}**")

            # رسم بياني
            st.subheader("📊 Total Sales per Product")
            if 'Sales' in df.columns:
                chart_data = df.groupby('Product')['Sales'].sum().reset_index()
                fig = px.bar(chart_data, x='Product', y='Sales', color='Product')
                st.plotly_chart(fig)
            else:
                st.warning("⚠️ 'Sales' column not found for plotting.")

            # الشات بوت البسيط
            st.subheader("💬 Smart Sales Chat")
            st.write("👎 اسأل سؤالك")
            question = st.selectbox("✍️ اختر استفسارك", [
                "كيف أزيد المبيعات؟",
                "ما هو المنتج الأفضل؟",
                "ما هو الفرع الأضعف؟",
                "ما هو التريند الحالي؟"
            ])

            if question == "كيف أزيد المبيعات؟":
                st.info("💡 روّج أكثر للمنتجات القوية، وقلل المنتجات الضعيفة، وحفّز الفروع الأقل أداء.")
            elif question == "ما هو المنتج الأفضل؟":
                st.info(f"🏆 المنتج الأفضل هو: **{top_product}**")
            elif question == "ما هو الفرع الأضعف؟":
                weakest_branch = df['Branch'].value_counts().idxmin()
                st.info(f"📉 أضعف فرع هو: **{weakest_branch}**")
            elif question == "ما هو التريند الحالي؟":
                st.info(f"📈 المنتجات الرائجة حاليًا: **{df['Product'].mode()[0]}**")

        else:
            st.warning("⚠️ Make sure your file includes 'Branch' and 'Product' columns.")
    except Exception as e:
        st.error(f"❌ Error loading file: {e}")
else:
    st.info("📁 Please upload a CSV file to begin.")
