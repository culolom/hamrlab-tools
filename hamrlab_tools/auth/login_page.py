import streamlit as st
from hamrlab_tools.auth.google_auth import google_login_button, verify_google_token
from hamrlab_tools.auth.session import login

def login_page():
    st.title("🔐 倉鼠工具登入系統")

    # --- 診斷：印出 google_login_button() 回傳內容 ---
    btn_html = google_login_button()
    st.write("DEBUG 按鈕 HTML：", btn_html)

    # --- 強制試著渲染 ---
    st.components.v1.html(btn_html, height=200)

    # 等待 Google 回傳 token
    token = st.experimental_get_query_params().get("token", None)

    if token:
        user = verify_google_token(token[0])
        if user:
            login(user)
            st.experimental_set_query_params()
            st.rerun()

    st.info("請使用 Google 帳號登入")
