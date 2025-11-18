import streamlit as st
from hamrlab_tools.auth.google_auth import google_login_button, verify_google_token
from hamrlab_tools.auth.session import login


def login_page():
    st.title("🔐 倉鼠工具登入系統")

    # 按鈕 HTML
    btn_html = google_login_button()
    st.components.v1.html(btn_html, height=120)

    # Google OAuth 回傳 access_token
    params = st.experimental_get_query_params()

    access_token = params.get("access_token", [None])[0]

    if access_token:
        user = verify_google_token(access_token)

        if user:
            login(user)
            st.experimental_set_query_params()   # 清空網址參數
            st.rerun()

    st.info("請使用 Google 帳號登入")
