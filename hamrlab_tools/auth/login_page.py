import streamlit as st
from hamrlab_tools.auth.google_auth import google_login_button, verify_google_token
from hamrlab_tools.auth.session import login

def login_page():
    st.title("🔐 倉鼠工具登入系統")

    google_login_button()

    # Google 回傳 access_token 會放在 URL hash 中
    token = st.query_params.get("access_token")

    if token:
        user = verify_google_token(token)
        if user:
            login(user)
            st.query_params.clear()
            st.rerun()

    st.info("請使用 Google 帳號登入")
