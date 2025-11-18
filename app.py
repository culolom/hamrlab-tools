import streamlit as st

from hamster_tools.auth.session import init_session, is_logged_in
from hamster_tools.auth.login_page import login_page
from hamster_tools.auth.logout import logout_button


def main():

    # 初始化 Session
    init_session()

    # 顯示登入頁
    if not is_logged_in():
        login_page()
        st.stop()

    # 已登入 → 顯示主頁
    st.sidebar.success(f"👋 歡迎：{st.session_state['user']['email']}")
    logout_button()

    st.title("倉鼠投資工具平台")
    st.write("請從左側選擇功能")

main()
