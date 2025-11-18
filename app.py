import streamlit as st
import urllib.parse

GOOGLE_CLIENT_ID = st.secrets["google"]["client_id"]

# 你的正式 redirect URL
REDIRECT_URI = "https://hamrlab-tools-n8h6issmc9pjq9vq6kzptn.streamlit.app/"

def google_login_button():
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"

    params = {
        "response_type": "token",
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "openid email profile",
        "prompt": "select_account"
    }

    auth_url = f"{base_url}?{urllib.parse.urlencode(params)}"

    html = f"""
    <style>
        .google-btn {{
            display: inline-flex;
            align-items: center;
            background-color: white;
            border: 1px solid #dadce0;
            padding: 12px 24px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 18px;
            color: #3c4043;
            font-weight: 500;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }}
        .google-btn:hover {{
            background-color: #f7f8f8;
        }}
        .google-icon {{
            height: 24px;
            margin-right: 12px;
        }}
    </style>
    <a href="{auth_url}">
        <div class="google-btn">
            <img class="google-icon" src="https://developers.google.com/identity/images/g-logo.png">
            使用 Google 帳號登入
        </div>
    </a>
    """

    st.markdown(html, unsafe_allow_html=True)


def verify_google_token(token):
    """
    前端使用 response_type=token 回傳的 token
    格式是 access_token，需要調 Google API 取 userinfo
    """
    import requests

    url = "https://www.googleapis.com/oauth2/v3/userinfo"
    headers = {"Authorization": f"Bearer {token}"}

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r.json()  # {email, name, picture, sub}
    return None
