import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; overflow: hidden; }
    
    .card { 
        position: relative;
        background: transparent; 
        border: 1px solid rgba(150, 150, 150, 0.2); 
        border-radius: 40px; 
        padding: 60px 30px 30px 30px;
    }
    
    .major-title { 
        position: absolute;
        top: 25px;
        left: 30px;
        font-weight: 600; 
        font-size: 1.1rem; 
        color: #888; 
    }
    
    /* ボタンを左上に配置 */
    div.stButton > button { 
        background: transparent !important; 
        border: none !important; 
        color: #888 !important; 
        font-size: 2rem !important; 
        padding: 0 !important;
        position: absolute;
        top: 20px;
        right: 30px;
    }

    /* メーターを完全に中央寄せ */
    .gauge-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 75vh;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

def create_gauge():
    fig = go.Figure()
    fig.add_trace(go.Pie(values=[50, 50], hole=0.55, marker=dict(colors=['#E0E0E0', '#E0E0E0']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    # 余白を極限までゼロにする
    fig.update_layout(width=250, height=250, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('<div class="card" style="height: 75vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">Civil Engineering</div>', unsafe_allow_html=True)
    if st.button("+"): st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # 新しいCSSクラスで囲んで強制中央寄せ
    st.markdown('<div class="gauge-wrapper">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(), use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card" style="height: 36vh; margin-bottom: 3vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">East Asian Studies</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card" style="height: 36vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">Wishlist</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
