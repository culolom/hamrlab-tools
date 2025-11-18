import streamlit as st
import urllib.parse

def google_login_button():
    GOOGLE_CLIENT_ID = st.secrets["google"]["client_id"]
    REDIRECT_URI = st.secrets["google"]["redirect_uri"]

    params = {
        "response_type": "token",
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "openid email profile",
        "prompt": "select_account"
    }

    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)

    # 這裡改成正常<a>按鈕，不用 iframe
    btn_html = f"""
    <style>
        .google-login-btn {{
            display: inline-flex;
            align-items: center;
            padding: 10px 20px;
            border-radius: 6px;
            background-color: white;
            border: 1px solid #dadce0;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
            color: #3c4043;
            font-weight: 500;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}
        .google-login-btn:hover {{
            background-color: #f7f8f8;
        }}
        .google-icon {{
            height: 20px;
            margin-right: 10px;
        }}
    </style>

    <a class="google-login-btn" href="{auth_url}" target="_blank">
        <img class="google-icon"
        src="https://developers.google.com/identity/images/g-logo.png" />
        使用 Google 帳號登入
    </a>
    """
    return btn_html


def verify_google_token(access_token: str):
    import requests
    url = f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={access_token}"
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    return None
