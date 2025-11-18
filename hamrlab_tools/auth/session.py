import streamlit as st


def init_session():
    if "user" not in st.session_state:
        st.session_state["user"] = None


def login(user_info: dict):
    st.session_state["user"] = user_info


def logout():
    st.session_state["user"] = None


def is_logged_in():
    return st.session_state.get("user") is not None
