import streamlit as st
import streamlit.components.v1 as components

st.title("🛡️ Faveiro — Анализ репутации")
st.header("📊 Отзывы клиентов")

uploaded_file = st.file_uploader("📁 Выберите HTML/CSV с отзывами", type=['html','csv','txt'])

if uploaded_file is not None:
    st.success(f"✅ Загружен: {uploaded_file.name}")
    content = uploaded_file.read().decode('utf-8', errors='ignore')
    components.html(content, height=800, scrolling=True)
