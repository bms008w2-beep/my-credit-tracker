import streamlit as st
import json
import plotly.graph_objects as go
from github import Github

# --- Settings ---
# (中略: G_USER, G_REPO等は適宜設定してください)
st.set_page_config(page_title="Credit Dashboard", layout="wide")

# CSS: スクロールバー排除、MacBookフィットデザイン
st.markdown("""
    <style>
    /* スクロールバーを消す */
    ::-webkit-scrollbar { display: none; }
    .stApp { background-color: #FDFBF7; }
    
    .card { 
        background-color: transparent; 
        padding: 30px; 
        border-radius: 40px; 
        border: 1px solid rgba(200, 200, 200, 0.3); 
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
    }
    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #444; }
    
    /* ボタンの透明化 */
    div.stButton > button {
        background-color: transparent !important;
        border: 1px solid #ccc !important;
        border-radius: 20px !important;
        color: #444 !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- Gauge Function (非常に太いリング) ---
def create_gauge(civil, ea):
    fig = go.Figure()
    # holeを0.55にすることで、よりリング幅を太く
    fig.add_trace(go.Pie(values=[50, 50], hole=0.55, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    
    def get_green(ratio): 
        return f'rgb({int(100 - 50 * ratio)}, {int(180 + 75 * ratio)}, {int(120 + 80 * ratio)})'

    c_perc = min(civil / 64, 1.0)
    for i in range(50):
        if i/50 < c_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.55, marker=dict(colors=[get_green(i/50), 'rgba(0,0,0,0)']), rotation=90 - (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    e_perc = min(ea / 64, 1.0)
    for i in range(50):
        if i/50 < e_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.55, marker=dict(colors=[get_green(i/50), 'rgba(0,0,0,0)']), rotation=90 + (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    fig.update_layout(width=280, height=280, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- Layout ---
col_l, col_c, col_r = st.columns([1, 1, 1])

# 中央のメーターを最大限活かす
with col_c:
    st.markdown('<div class="card" style="align-items:center; border:none;">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(0, 0), use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

# 左と右で学科を分ける
with col_l:
    st.markdown('<div class="card"><div class="major-title">Civil Engineering</div></div>', unsafe_allow_html=True)
    if st.button("+"): st.session_state.show_add = True

with col_r:
    st.markdown('<div class="card"><div class="major-title">East Asian Studies</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="major-title">Wishlist</div></div>', unsafe_allow_html=True)
