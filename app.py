import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard", layout="wide")

# CSS: 全ての要素を画面の指定座標に強制配置
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    /* 不要な余白を全消去 */
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    .container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px;
        height: 95vh;
    }
    
    .card {
        border: 1px solid rgba(150, 150, 150, 0.2);
        border-radius: 40px;
        padding: 30px;
        position: relative;
    }
    
    .title { color: #888; font-weight: 600; font-size: 1.2rem; }
    
    /* ボタンを消してカスタム配置 */
    .plus-btn { position: absolute; top: 20px; right: 30px; cursor: pointer; color: #888; font-size: 2rem; }
    </style>
""", unsafe_allow_html=True)

# 画面全体をコンテナで覆う
st.markdown('<div class="container">', unsafe_allow_html=True)

# 1. Civil Engineering (左)
st.markdown('<div class="card"><div class="title">Civil Engineering</div>', unsafe_allow_html=True)
if st.button("+", key="btn1"): st.session_state.show_add = True
st.markdown('</div>', unsafe_allow_html=True)

# 2. メーター (中央)
fig = go.Figure()
fig.add_trace(go.Pie(values=[50, 50], hole=0.55, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
fig.update_layout(width=250, height=250, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, use_container_width=False)

# 3. 右側列
st.markdown('<div style="display:grid; grid-template-rows: 1fr 1fr; gap: 20px;">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="title">East Asian Studies</div></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="title">Wishlist</div></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)
