import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
    <style>
    /* 画面全体の余白を極限までカット */
    .block-container { padding: 20px !important; }
    .stApp { background-color: #FDFBF7; overflow: hidden; }

    /* 3カラムを完全に均等化するGrid設定 */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        height: 85vh;
    }

    .card { 
        position: relative;
        background: transparent; 
        border: 1px solid rgba(150, 150, 150, 0.2); 
        border-radius: 40px; 
        padding: 20px;
    }

    .major-title { 
        font-weight: 600; font-size: 1.1rem; color: #888;
        margin-bottom: 10px;
    }

    /* メーターを親要素に対して絶対的な中央へ */
    .gauge-center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        width: 100%;
    }
    
    div.stButton > button { 
        background: transparent !important; 
        border: none !important; 
        color: #888 !important; 
        font-size: 2rem !important; 
        padding: 0 !important;
        position: absolute; top: 10px; right: 20px;
    }
    </style>
""", unsafe_allow_html=True)

def create_gauge():
    fig = go.Figure()
    fig.add_trace(go.Pie(values=[50, 50], hole=0.55, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    fig.update_layout(width=280, height=280, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# Gridレイアウト開始
st.markdown('<div class="grid-container">', unsafe_allow_html=True)

# 1. Civil Engineering
st.markdown('<div class="card" style="grid-row: span 2;">', unsafe_allow_html=True)
st.markdown('<div class="major-title">Civil Engineering</div>', unsafe_allow_html=True)
if st.button("+"): st.session_state.show_add = True
st.markdown('</div>', unsafe_allow_html=True)

# 2. Gauge (中央)
st.markdown('<div class="gauge-center">', unsafe_allow_html=True)
st.plotly_chart(create_gauge(), use_container_width=False)
st.markdown('</div>', unsafe_allow_html=True)

# 3. Right side (East Asian + Wishlist)
st.markdown('<div>', unsafe_allow_html=True)
st.markdown('<div class="card" style="height: 48%; margin-bottom: 20px;"><div class="major-title">East Asian Studies</div></div>', unsafe_allow_html=True)
st.markdown('<div class="card" style="height: 48%;"><div class="major-title">Wishlist</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
