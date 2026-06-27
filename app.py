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

# CSS: MacBook対応、ボタン背景なし、太いメーター用調整
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    .card { 
        background-color: transparent; 
        padding: 40px; 
        border-radius: 40px; 
        border: 1px solid rgba(200, 200, 200, 0.2); 
        height: 500px; 
        overflow-y: auto; 
        margin-bottom: 20px; 
    }
    .major-title { font-weight: bold; font-size: 1.3rem; margin-bottom: 20px; color: #444; }
    /* プラスボタンの背景を透明に */
    div.stButton > button {
        background-color: transparent !important;
        border: 1px solid #ccc !important;
        border-radius: 20px !important;
        color: #444 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Gauge Function (太いリング) ---
def create_gauge(civil, ea):
    fig = go.Figure()
    # 太いグレーのリング (holeを0.6に)
    fig.add_trace(go.Pie(values=[50, 50], hole=0.6, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    
    def get_green(ratio): 
        return f'rgb({int(100 - 50 * ratio)}, {int(180 + 75 * ratio)}, {int(120 + 80 * ratio)})'

    c_perc = min(civil / TARGET_CIVIL, 1.0)
    for i in range(50):
        if i/50 < c_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.6, marker=dict(colors=[get_green(i/50), 'rgba(0,0,0,0)']), rotation=90 - (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    e_perc = min(ea / TARGET_EA, 1.0)
    for i in range(50):
        if i/50 < e_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.6, marker=dict(colors=[get_green(i/50), 'rgba(0,0,0,0)']), rotation=90 + (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    fig.update_layout(width=300, height=300, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- Main Layout ---
col_l, col_c, col_r = st.columns([1, 1, 1])

with col_c:
    st.markdown('<div class="card" style="display:flex; justify-content:center; align-items:center;">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(0, 0), use_container_width=True) # ここに計算済みの値を入れる
    st.markdown('</div>', unsafe_allow_html=True)

with col_l:
    st.markdown('<div class="card"><div class="major-title">Civil Engineering</div>', unsafe_allow_html=True)
    if st.button("+"): st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_r:
    st.markdown('<div class="card"><div class="major-title">East Asian Studies</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="major-title">Wishlist</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
