import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard", layout="wide")

# Streamlit特有の余白を強制的に消去
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    /* メインコンテナの余白を消去 */
    .block-container { max-width: 95% !important; padding: 20px !important; }
    
    /* 画面全体を3等分するGrid */
    .dashboard {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 20px;
        height: 85vh;
    }
    
    .card { 
        border: 1px solid rgba(150, 150, 150, 0.2); 
        border-radius: 40px; 
        padding: 30px;
        background: transparent;
        position: relative;
    }

    .title { color: #888; font-weight: 600; margin-bottom: 20px; }
    
    /* ボタンの位置固定 */
    .plus-btn { position: absolute; top: 20px; right: 30px; font-size: 2rem; }
    
    /* 右側の列を上下に分ける */
    .right-col { display: grid; grid-template-rows: 1fr 1fr; gap: 20px; }
    </style>
""", unsafe_allow_html=True)

def create_gauge():
    fig = go.Figure()
    fig.add_trace(go.Pie(values=[50, 50], hole=0.55, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    fig.update_layout(width=300, height=300, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- 描画 ---
st.markdown('<div class="dashboard">', unsafe_allow_html=True)

# 1. 土木 (左列)
st.markdown('''<div class="card">
    <div class="title">Civil Engineering</div>
''', unsafe_allow_html=True)
if st.button("+", key="c"): st.session_state.show_add = True
st.markdown('</div>', unsafe_allow_html=True)

# 2. メーター (中央列)
st.markdown('<div style="display:flex; justify-content:center; align-items:center;">', unsafe_allow_html=True)
st.plotly_chart(create_gauge(), use_container_width=False)
st.markdown('</div>', unsafe_allow_html=True)

# 3. 東アジアとWishlist (右列)
st.markdown('<div class="right-col">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="title">East Asian Studies</div></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="title">Wishlist</div></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)
