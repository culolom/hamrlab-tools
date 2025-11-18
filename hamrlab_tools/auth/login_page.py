import streamlit as st
from hamrlab_tools.auth.google_auth import google_login_button, verify_google_token
from hamrlab_tools.auth.session import login


def login_page():
    st.title("🔐 倉鼠工具登入系統")

    google_login_button()

    # 等待前端回傳 token
    message = st.experimental_get_query_params().get("token", None)

    if message:
        user = verify_google_token(message[0])
        if user:
            login(user)
            st.experimental_set_query_params()  # 清除 token
            st.rerun()

    st.info("請使用 Google 帳號登入")

