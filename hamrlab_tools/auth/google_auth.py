import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests

GOOGLE_CLIENT_ID = st.secrets["google"]["client_id"]


def google_login_button():
    st.markdown("""
        <div id="g_id_onload"
             data-client_id="{client_id}"
             data-context="signin"
             data-ux_mode="popup"
             data-callback="onSignIn">
        </div>

        <div class="g_id_signin"
             data-type="standard"
             data-size="large">
        </div>

        <script>
        function onSignIn(response) {{
            const token = response.credential;
            window.parent.postMessage({{ type: 'google_login', token: token }}, "*");
        }}
        </script>

        <script src="https://accounts.google.com/gsi/client" async defer></script>
    """.format(client_id=GOOGLE_CLIENT_ID),
    unsafe_allow_html=True)


def verify_google_token(token: str):
    try:
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), GOOGLE_CLIENT_ID
        )
        return {
            "email": idinfo["email"],
            "name": idinfo.get("name", ""),
            "picture": idinfo.get("picture", "")
        }
    except Exception:
        return None
