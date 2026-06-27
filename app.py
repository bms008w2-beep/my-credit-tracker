import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; overflow: hidden; }
    
    /* カードの設定: 横幅を3等分（均等）にするための調整 */
    .card { 
        background: transparent; 
        border: 1px solid rgba(150, 150, 150, 0.2); 
        border-radius: 40px; 
        padding: 30px;
        display: flex;
        flex-direction: column;
        color: #777; /* 文字色を少し薄くして透明感に合わせる */
    }
    
    /* 題名の文字色を薄くし、背景に溶け込ませる */
    .major-title { 
        font-weight: 600; 
        font-size: 1.1rem; 
        margin-bottom: 15px; 
        color: #888; 
    }
    
    div.stButton > button { 
        background: transparent !important; 
        border: none !important; 
        color: #888 !important; 
        font-size: 2rem !important; 
        padding: 0 !important; 
    }
    </style>
""", unsafe_allow_html=True)

def create_gauge():
    fig = go.Figure()
    fig.add_trace(go.Pie(values=[50, 50], hole=0.55, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    fig.update_layout(width=250, height=250, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# 横幅を均等に3分割
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('<div class="card" style="height: 75vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">Civil Engineering</div>', unsafe_allow_html=True)
    if st.button("+"): st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # 中央にメーターを配置（左右の列と高さを合わせる）
    st.markdown('<div style="display:flex; justify-content:center; align-items:center; height:75vh;">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(), use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    # 右列を上下に分割（合計75vhになるように調整）
    st.markdown('<div class="card" style="height: 36vh; margin-bottom: 3vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">East Asian Studies</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card" style="height: 36vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">Wishlist</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
