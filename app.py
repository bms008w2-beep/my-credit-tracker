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

# --- Initialize Session State ---
if "units" not in st.session_state:
    st.session_state.units = []
    try:
        # GitHubからデータを取得
        repo = Github(st.secrets["GITHUB_TOKEN"]).get_repo(f"{G_USER}/{G_REPO}")
        content = repo.get_contents("data.json")
        st.session_state.units = json.loads(content.decoded_content.decode("utf-8"))
    except Exception as e:
        st.warning("Could not load data from GitHub. Starting with empty list.")

# --- Functions ---
def create_gauge(civil, ea):
    fig = go.Figure()
    fig.add_trace(go.Pie(values=[50, 50], hole=0.9, marker=dict(colors=['#FDF0F0', '#FDF0F0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    
    def get_lavender(ratio): 
        return f'rgb({int(180 + 50 * ratio)}, {int(160 + 40 * ratio)}, {int(230 + 25 * ratio)})'

    c_perc = min(civil / TARGET_CIVIL, 1.0)
    for i in range(50):
        if i/50 < c_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.9, marker=dict(colors=[get_lavender(i/50), 'rgba(0,0,0,0)']), rotation=90 - (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
            
    e_perc = min(ea / TARGET_EA, 1.0)
    for i in range(50):
        if i/50 < e_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.9, marker=dict(colors=[get_lavender(i/50), 'rgba(0,0,0,0)']), rotation=90 + (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    fig.update_layout(width=250, height=250, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- UI Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    .card { background-color: transparent; padding: 30px; border-radius: 40px; border: 1px solid rgba(200, 200, 200, 0.2); margin-bottom: 20px; }
    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #555; }
    </style>
""", unsafe_allow_html=True)

# --- Calculations ---
civil_units = sum(int(u['credits']) for u in st.session_state.units if u.get('major') == "Civil Engineering")
ea_units = sum(int(u['credits']) for u in st.session_state.units if u.get('major') == "East Asian Studies")

# --- Layout ---
col_l, col_c, col_r = st.columns([1, 1.2, 1])

with col_c:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(civil_units, ea_units), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_l:
    st.markdown(f'<div class="card"><div class="major-title">Civil Engineering ({civil_units}/{TARGET_CIVIL})</div>', unsafe_allow_html=True)
    for u in [x for x in st.session_state.units if x.get('major') == "Civil Engineering"]: st.write(f"- {u['name']} ({u['credits']})")
    if st.button("+"): st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

# Add form
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
    for u in [x for x in st.session_state.units if x.get('major') == "East Asian Studies"]: st.write(f"- {u['name']} ({u['credits']})")
    st.markdown('</div>', unsafe_allow_html=True)
