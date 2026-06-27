import streamlit as st

# 設定: 画面を広々と使う
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS: 画面全体を固定し、スクロールを無効化
st.markdown("""
    <style>
    /* 全体を固定してスクロールを出さない */
    .block-container { max-width: 95% !important; padding-top: 20px !important; }
    
    /* コンテナの親要素 */
    .dashboard-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr; /* 左(土木)を大きく */
        gap: 20px;
        height: 85vh; /* 画面内に収める */
    }

    /* 各カードの共通スタイル */
    .card {
        background-color: transparent;
        border: 1px solid rgba(200, 200, 200, 0.3);
        border-radius: 40px;
        padding: 30px;
        display: flex;
        flex-direction: column;
        overflow-y: auto; /* 中身が増えたらここだけでスクロール */
    }

    /* 右側の列（東アジアとWishlist）を縦に並べる設定 */
    .right-stack {
        display: grid;
        grid-template-rows: 1fr 1fr;
        gap: 20px;
    }

    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #444; }
    
    /* ボタンの枠と背景を完全消去 */
    div.stButton > button {
        background-color: transparent !important;
        border: none !important;
        color: #444 !important;
        font-size: 2rem !important;
        padding: 0 !important;
        box-shadow: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- レイアウト構築 ---
st.markdown('<div class="dashboard-grid">', unsafe_allow_html=True)

# 1. 土木 (2倍の高さ/広さ)
st.markdown('''
    <div class="card">
        <div class="major-title">Civil Engineering</div>
''', unsafe_allow_html=True)
if st.button("+"): st.session_state.show_add = True
st.markdown('</div>', unsafe_allow_html=True)

# 2. 中央メーター
st.markdown('''
    <div class="card" style="justify-content:center; align-items:center;">
        </div>
''', unsafe_allow_html=True)

# 3. 右側 (東アジア + Wishlist)
st.markdown('<div class="right-stack">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="major-title">East Asian Studies</div></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="major-title">Wishlist</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
