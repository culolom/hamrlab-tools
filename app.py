import streamlit as st

from hamrlab_tools.auth.session import init_session, is_logged_in
from hamrlab_tools.auth.login_page import login_page
from hamrlab_tools.auth.logout import logout_button
from hamrlab_tools.auth.google_auth import google_login_button, verify_google_token

# 初始化 session
init_session()

# 未登入 → 顯示登入頁
if not is_logged_in():
    login_page()
    st.stop()

# 已登入 → 顯示主系統
st.sidebar.write(f"👋 歡迎：{st.session_state['user']['email']}")
logout_button()

st.title("HamrLab 投資工具平台")
st.write("請從左側選單選擇功能")
