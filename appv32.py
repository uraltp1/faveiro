import streamlit as st

st.title("🛡️ Faveiro — Анализ репутации")
st.header("📊 Отзывы клиентов")

uploaded_file = st.file_uploader("📁 Выберите HTML/CSV с отзывами", type=['html','csv','txt'])

if uploaded_file is not None:
    st.success(f"✅ Загружен: {uploaded_file.name}")
    content = uploaded_file.read().decode('utf-8', errors='ignore')
    st.text_area("📄 Содержимое файла:", content, height=500)
