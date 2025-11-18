import streamlit as st
from hamrlab_tools.auth.google_auth import google_login_button, verify_google_token
from hamrlab_tools.auth.session import login

def login_page():
    st.title("🔐 倉鼠工具登入系統")

    # 取得登入按鈕的 HTML
    html_button = google_login_button()

    # 顯示 Google 登入按鈕
    st.components.v1.html(html_button, height=80)

    # 等待 Google 回傳 token
    token = st.experimental_get_query_params().get("token", None)

    if token:
        user = verify_google_token(token[0])
        if user:
            login(user)
            st.experimental_set_query_params()  # 清除 query string
            st.rerun()

    st.info("請使用 Google 帳號登入")
