import streamlit as st
import urllib.parse

# 從 secrets 取 Google OAuth 設定
GOOGLE_CLIENT_ID = st.secrets["google"]["client_id"]
GOOGLE_REDIRECT_URI = st.secrets["google"]["redirect_uri"]
GOOGLE_SCOPE = "openid email profile"

def google_login_button():
    """
    回傳 Google Oauth 登入按鈕 HTML
    """
    params = {
        "response_type": "token",
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "scope": GOOGLE_SCOPE,
        "prompt": "select_account"
    }

    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)

    # 給 Streamlit 用的按鈕 HTML
    button_html = f"""
    <style>
        .google-btn {{
            display: inline-flex;
            align-items: center;
            background-color: white;
            border: 1px solid #dadce0;
            padding: 10px 20px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            color: #3c4043;
            font-weight: 500;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }}
        .google-btn:hover {{
            background-color: #f7f8f8;
        }}
        .google-icon {{
            height: 20px;
            margin-right: 10px;
        }}
    </style>

    <a href="{auth_url}" target="_self">
        <div class="google-btn">
            <img class="google-icon" src="https://developers.google.com/identity/images/g-logo.png" />
            使用 Google 帳號登入
        </div>
    </a>
    """

    return button_html


def verify_google_token(access_token):
    """
    驗證 Google Access Token 並回傳使用者資訊
    """
    import requests

    google_api = "https://www.googleapis.com/oauth2/v3/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}

    resp = requests.get(google_api, headers=headers)

    if resp.status_code == 200:
        return resp.json()
    else:
        return None
