import streamlit as st

def init_theme():
    # 預設主題
    if "theme" not in st.session_state:
        st.session_state["theme"] = "light"

    theme = st.session_state["theme"]

    if theme == "dark":
        bg_color = "#050816"
        card_bg = "#111827"
        text_color = "#F9FAFB"
        accent = "#22c55e"
    else:
        bg_color = "#F3F4F6"
        card_bg = "#FFFFFF"
        text_color = "#111827"
        accent = "#2563eb"

    css = f"""
    <style>
    /* 取消預設 padding，讓版面更像 SaaS */
    .main {{
        background: {bg_color};
        color: {text_color};
    }}
    .stApp {{
        background: {bg_color};
    }}
    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: #020617;
        color: #E5E7EB;
    }}
    section[data-testid="stSidebar"] * {{
        color: #E5E7EB !important;
    }}
    /* 卡片 */
    .hamster-card {{
        background: {card_bg};
        padding: 1.2rem 1.4rem;
        border-radius: 1.1rem;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12);
        border: 1px solid rgba(148, 163, 184, 0.25);
        margin-bottom: 1rem;
    }}
    .hamster-kpi {{
        background: {card_bg};
        padding: 0.8rem 1rem;
        border-radius: 0.9rem;
        border: 1px solid rgba(148, 163, 184, 0.35);
    }}
    .hamster-badge {{
        display: inline-block;
        padding: 0.15rem 0.6rem;
        border-radius: 999px;
        font-size: 0.75rem;
        background: rgba(37, 99, 235, 0.12);
        color: {accent};
        border: 1px solid rgba(96, 165, 250, 0.6);
    }}
    /* 表格字顏色修正 */
    .hamster-table tbody td {{
        font-size: 0.86rem;
    }}
    /* 手機版：改為單欄 */
    @media (max-width: 768px) {{
        .block-container {{
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }}
    }}
    /* （可選）隱藏右上角一些 icon
    button[kind="icon"] {{
        display: none !important;
    }}
    footer {{visibility: hidden;}}
    */
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    return theme
