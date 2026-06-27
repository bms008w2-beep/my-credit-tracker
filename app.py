import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

# CSS: スクロールを消し、カードの角丸や透明度を調整
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    
    /* カードのスタイル: 高さを揃えるための設定 */
    .card { 
        background: transparent; 
        border: 1px solid rgba(200, 200, 200, 0.3); 
        border-radius: 40px; 
        padding: 30px; 
        margin-bottom: 20px;
    }
    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #444; }
    </style>
""", unsafe_allow_html=True)

# 左右の列を作成（1:1の比率）
col1, col2 = st.columns([1, 1])

with col1:
    # 土木のカード（高さを大きく確保）
    st.markdown('<div class="card" style="height: 70vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">Civil Engineering</div>', unsafe_allow_html=True)
    if st.button("+", key="civil_btn"): st.session_state.show_add = True
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # 東アジア（上段）
    st.markdown('<div class="card" style="height: 33vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">East Asian Studies</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Wishlist（下段）
    st.markdown('<div class="card" style="height: 33vh;">', unsafe_allow_html=True)
    st.markdown('<div class="major-title">Wishlist</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
