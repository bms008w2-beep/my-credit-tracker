import streamlit as st
import json
import plotly.graph_objects as go
from github import Github

# --- Settings ---
# (GitHub設定等は適宜環境に合わせてください)
st.set_page_config(page_title="Credit Dashboard", layout="wide")

# CSS: 完全な中央配置、固定高、枠なしボタン
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    
    /* カードのスタイル: 高さを固定して枠内でスクロール */
    .card { 
        background-color: transparent; 
        padding: 30px; 
        border-radius: 40px; 
        border: 1px solid rgba(200, 200, 200, 0.3); 
        height: 350px; 
        overflow-y: auto;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
    }
    
    /* メーター用コンテナ */
    .gauge-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 350px;
    }
    
    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #444; }
    
    /* プラスボタンの背景と枠を完全消去 */
    div.stButton > button {
        background-color: transparent !important;
        border: none !important;
        color: #444 !important;
        font-size: 2rem !important;
        padding: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Gauge Function ---
def create_gauge(civil, ea):
    fig = go.Figure()
    fig.add_trace(go.Pie(values=[50, 50], hole=0.55, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    
    def get_green(ratio): return f'rgb(80, 180, 120)'
    
    # 簡易的にセグメントを追加
    for i in range(50):
        if i/50 < min(civil/64, 1.0):
            fig.add_trace(go.Pie(values=[1, 199], hole=0.55, marker=dict(colors=[get_green(i/50), 'rgba(0,0,0,0)']), rotation=90 - (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    fig.update_layout(width=300, height=300, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- Layout ---
col_l, col_c, col_r = st.columns([1, 1, 1])

# 中央配置の確定
with col_c:
    st.markdown('<div class="gauge-container">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(0, 0), use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

with col_l:
    st.markdown('<div class="card"><div class="major-title">Civil Engineering</div>', unsafe_allow_html=True)
    # ここに授業リスト
    if st.button("+"): st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_r:
    st.markdown('<div class="card"><div class="major-title">East Asian Studies</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="major-title">Wishlist</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 登録フォームの処理
if st.session_state.get("show_add"):
    with st.form("add_course"):
        name = st.text_input("Course Name")
        if st.form_submit_button("Submit"):
            st.session_state.show_add = False
            st.rerun()
