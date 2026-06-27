import streamlit as st
import json
import plotly.graph_objects as go
from github import Github

# --- Settings ---
G_USER = "YourGitHubUsername" 
G_REPO = "YourRepositoryName"
TARGET_CIVIL = 64
TARGET_EA = 64

st.set_page_config(page_title="Credit Dashboard", layout="wide")

# CSS: Lavender Theme, Transparent cards, Minimalist
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    /* 透明なカードデザイン */
    .card { 
        background-color: transparent; 
        padding: 30px; 
        border-radius: 40px; 
        border: 1px solid rgba(200, 200, 200, 0.2); 
        margin-bottom: 20px; 
    }
    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #555; }
    </style>
""", unsafe_allow_html=True)

# (Data Functions / create_gauge は前回のまま)

# Main UI
civil_units = sum(int(u['credits']) for u in st.session_state.units if u['major'] == "Civil Engineering")
ea_units = sum(int(u['credits']) for u in st.session_state.units if u['major'] == "East Asian Studies")

col_l, col_c, col_r = st.columns([1, 1.2, 1])

with col_c:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(civil_units, ea_units), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_l:
    st.markdown(f'<div class="card"><div class="major-title">Civil Engineering ({civil_units}/{TARGET_CIVIL})</div>', unsafe_allow_html=True)
    for u in [x for x in st.session_state.units if x['major'] == "Civil Engineering"]: st.write(f"- {u['name']} ({u['credits']})")
    
    # 左下にプラスボタン
    if st.button("+"):
        st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

# プラスボタンが押されたら入力フォームを表示
if st.session_state.get("show_add"):
    with st.form("add"):
        name = st.text_input("Course Name")
        major = st.selectbox("Major", ["Civil Engineering", "East Asian Studies"])
        cred = st.number_input("Credits", 1, 8)
        if st.form_submit_button("Submit"):
            st.session_state.units.append({"name": name, "major": major, "credits": cred})
            st.session_state.show_add = False
            st.rerun()

with col_r:
    st.markdown(f'<div class="card"><div class="major-title">East Asian Studies ({ea_units}/{TARGET_EA})</div>', unsafe_allow_html=True)
    for u in [x for x in st.session_state.units if x['major'] == "East Asian Studies"]: st.write(f"- {u['name']} ({u['credits']})")
    st.markdown('</div>', unsafe_allow_html=True)
