import streamlit as st
from bs4 import BeautifulSoup

st.title("🛡️ Faveiro — Анализ репутации")
st.header("📊 Отзывы клиентов")

uploaded_file = st.file_uploader("📁 Выберите HTML/CSV с отзывами", type=["html", "csv", "txt"])

if uploaded_file is not None:
    st.success(f"✅ Загружен: {uploaded_file.name}")
    content = uploaded_file.read().decode("utf-8", errors="ignore")

    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text("\n", strip=True)

    st.text_area("📄 Текст из файла:", text, height=600)
