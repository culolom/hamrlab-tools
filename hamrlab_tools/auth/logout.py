import streamlit as st
from hamster_tools.auth.session import logout


def logout_button():
    if st.sidebar.button("🚪 登出"):
        logout()
        st.rerun()
