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

# CSS: Minimalist, Fixed Height, Lavender/Green Theme
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    .card { 
        background-color: transparent; 
        padding: 30px; 
        border-radius: 40px; 
        border: 1px solid rgba(200, 200, 200, 0.2); 
        height: 400px; /* カードの高さを固定 */
        overflow-y: auto; /* 中身が増えたらスクロール */
        margin-bottom: 20px; 
    }
    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #555; }
    </style>
""", unsafe_allow_html=True)

# --- Logic (Data Loading/Saving) ---
# ※保存処理（save_data）も忘れずに実装してください
if "units" not in st.session_state:
    st.session_state.units = []

# --- Gauge Function (Green, Thick Border) ---
def create_gauge(civil, ea):
    fig = go.Figure()
    # 背景の太いグレーの縁
    fig.add_trace(go.Pie(values=[50, 50], hole=0.8, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    
    def get_green(ratio): 
        return f'rgb({int(100 - 50 * ratio)}, {int(180 + 75 * ratio)}, {int(120 + 80 * ratio)})'

    # Civil (Clockwise)
    c_perc = min(civil / TARGET_CIVIL, 1.0)
    for i in range(50):
        if i/50 < c_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.8, marker=dict(colors=[get_green(i/50), 'rgba(0,0,0,0)']), rotation=90 - (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    # East Asian (Counter-clockwise)
    e_perc = min(ea / TARGET_EA, 1.0)
    for i in range(50):
        if i/50 < e_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.8, marker=dict(colors=[get_green(i/50), 'rgba(0,0,0,0)']), rotation=90 + (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    fig.update_layout(width=250, height=250, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- Main UI ---
civil_units = sum(int(u['credits']) for u in st.session_state.units if u.get('major') == "Civil Engineering")
ea_units = sum(int(u['credits']) for u in st.session_state.units if u.get('major') == "East Asian Studies")

col_l, col_c, col_r = st.columns([1, 1.2, 1])

with col_c:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(civil_units, ea_units), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_l:
    st.markdown('<div class="card"><div class="major-title">Civil Engineering</div>', unsafe_allow_html=True)
    for u in [x for x in st.session_state.units if x.get('major') == "Civil Engineering"]: st.write(f"- {u['name']} ({u['credits']})")
    if st.button("+"): st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_r:
    st.markdown('<div class="card"><div class="major-title">East Asian Studies</div>', unsafe_allow_html=True)
    for u in [x for x in st.session_state.units if x.get('major') == "East Asian Studies"]: st.write(f"- {u['name']} ({u['credits']})")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><div class="major-title">Wishlist</div>', unsafe_allow_html=True)
    # ここにWishlistの表示
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.get("show_add"):
    # フォーム表示処理は前回同様
    pass
