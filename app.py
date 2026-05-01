import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Sales Analyzer")


lang = st.radio("اختر اللغة | Choose Language", ["English", "العربية"], horizontal=True)
is_ar = lang == "العربية"

   
texts = {
    "title": " محلل المبيعات الذكي" if is_ar else " Smart Sales Analyzer",
    "upload": "ارفع ملف CSV" if is_ar else "Upload CSV file",
    "success": " تم رفع الملف بنجاح!" if is_ar else " File uploaded successfully!",
    "preview": " معاينة البيانات" if is_ar else " Data Preview",
    "chart": "الرسم البياني حسب '{}'" if is_ar else " Sales by '{}'",
    "ask": "يمكنك سؤال الشات بوت:" if is_ar else " You can ask the chatbot:",
    "questions": [
        "ما هو أكثر فرع مبيعًا؟",
        "ما هو المنتج الأكثر مبيعًا؟",
        "ما هو أقل ربح؟"
    ] if is_ar else [
        "What is the top selling branch?",
        "What is the top selling product?",
        "What is the least profit?"
    ],
    "chat_response": " رد الشات بوت" if is_ar else " Chatbot Response",
    "input": "اكتب سؤالك هنا:" if is_ar else "Ask your question:",
    "unknown": " آسف، لم أفهم السؤال. جرب سؤالاً من القائمة أعلاه." if is_ar else " Sorry, I didn't understand. Try one of the listed questions.",
    "top": "الأعلى مبيعًا هو: {}" if is_ar else "Top selling {}: {}",
    "least": "الأقل ربحًا هو: {}" if is_ar else "Least profit {}: {}",
    "error": " خطأ: {}" if is_ar else " Error: {}"
}


st.title(texts["title"])
st.write(texts["upload"])

uploaded_file = st.file_uploader("", type=["csv"])

def detect_sales_column(df):
    keywords = ['total', 'sales', 'amount', 'revenue', 'profit', 'price']
    for col in df.columns:
        if any(k in col.lower() for k in keywords) and pd.api.types.is_numeric_dtype(df[col]):
            return col
    return None

def detect_category_column(df, sales_col):
    for col in df.columns:
        if col != sales_col and df[col].nunique() <= 10:
            return col
    return None

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='latin1')
        st.success(texts["success"])

        st.subheader(texts["preview"])
        st.dataframe(df)

        sales_col = detect_sales_column(df)
        category_col = detect_category_column(df, sales_col)

        if sales_col and category_col:
            st.subheader(texts["chart"].format(category_col))
            chart_data = df.groupby(category_col)[sales_col].sum().sort_values(ascending=False)
            fig, ax = plt.subplots()
            chart_data.plot(kind='bar', ax=ax)
            ax.set_ylabel(sales_col)
            ax.set_xlabel(category_col)
            st.pyplot(fig)

        st.subheader(texts["ask"])
        for q in texts["questions"]:
            st.markdown(f"- {q}")

        st.subheader(texts["chat_response"])
        question = st.text_input(texts["input"])
        if question:
            q = question.lower()
            if "top" in q or "الأكثر" in q:
                result = df.groupby(category_col)[sales_col].sum().idxmax()
                st.success(texts["top"].format(category_col.lower(), result))
            elif "least" in q or "أقل" in q or "الربح" in q:
                result = df.groupby(category_col)[sales_col].sum().idxmin()
                st.success(texts["least"].format(category_col.lower(), result))
            else:
                st.info(texts["unknown"])
    except Exception as e:
        st.error(texts["error"].format(str(e)))
