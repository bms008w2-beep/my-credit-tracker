import streamlit as st
import json
import plotly.graph_objects as go
from github import Github

# --- 設定 ---
G_USER = "あなたのGitHubユーザー名" 
G_REPO = "作成したリポジトリ名"
TARGET_CIVIL = 64
TARGET_EA = 64

st.set_page_config(page_title="Credit Dashboard", layout="wide")

# CSS: クリーム色背景と角丸カードデザイン
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    .card { background-color: #FFFFFF; padding: 20px; border-radius: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .major-title { font-weight: bold; font-size: 1.2rem; margin-bottom: 15px; color: #333; }
    </style>
""", unsafe_allow_html=True)

# データ読み込み・保存
def get_repo():
    return Github(st.secrets["GITHUB_TOKEN"]).get_repo(f"{G_USER}/{G_REPO}")

if "units" not in st.session_state:
    try:
        content = get_repo().get_contents("data.json")
        st.session_state.units = json.loads(content.decoded_content.decode("utf-8"))
    except:
        st.session_state.units = []

# 円形メーターの生成
def create_gauge(civil, ea):
    fig = go.Figure()
    # 背景円
    fig.add_trace(go.Pie(values=[50, 50], hole=0.8, marker=dict(colors=['#eee', '#eee']), rotation=90, showlegend=False, hoverinfo='none', textinfo='none'))
    
    # グラデーション計算用
    def get_color(ratio): return f'rgb(0,{int(150 + 105 * ratio)},{int(127 + 128 * ratio)})'

    # 土木（時計回り）
    c_perc = min(civil / TARGET_CIVIL, 1.0)
    for i in range(50):
        if i/50 < c_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.82, marker=dict(colors=[get_color(i/50), 'rgba(0,0,0,0)']), rotation=90 - (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
            
    # 東アジア（反時計回り）
    e_perc = min(ea / TARGET_EA, 1.0)
    for i in range(50):
        if i/50 < e_perc:
            fig.add_trace(go.Pie(values=[1, 199], hole=0.82, marker=dict(colors=[get_color(i/50), 'rgba(0,0,0,0)']), rotation=90 + (180 * i/50), showlegend=False, hoverinfo='none', textinfo='none'))
    
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- メイン画面 ---
civil_units = sum(int(u['credits']) for u in st.session_state.units if u['major'] == "土木学科")
ea_units = sum(int(u['credits']) for u in st.session_state.units if u['major'] == "東アジア学科")

col_l, col_c, col_r = st.columns([1, 1.2, 1])

with col_c:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.plotly_chart(create_gauge(civil_units, ea_units), use_container_width=True)
    st.markdown(f'<h2 style="text-align:center">{civil_units + ea_units} / {TARGET_CIVIL + TARGET_EA}</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_l:
    st.markdown(f'<div class="card"><div class="major-title">🏗️ 土木学科 ({civil_units}/{TARGET_CIVIL})</div>', unsafe_allow_html=True)
    for u in [x for x in st.session_state.units if x['major'] == "土木学科"]: st.write(f"・{u['name']} ({u['credits']})")
    st.markdown('</div>', unsafe_allow_html=True)

with col_r:
    st.markdown(f'<div class="card"><div class="major-title">🌏 東アジア学科 ({ea_units}/{TARGET_EA})</div>', unsafe_allow_html=True)
    for u in [x for x in st.session_state.units if x['major'] == "東アジア学科"]: st.write(f"・{u['name']} ({u['credits']})")
    st.markdown('</div>', unsafe_allow_html=True)
    
    with st.expander("📝 授業を追加"):
        with st.form("add", clear_on_submit=True):
            name = st.text_input("授業名")
            major = st.selectbox("学科", ["土木学科", "東アジア学科"])
            cred = st.number_input("単位数", 1, 8)
            if st.form_submit_button("登録"):
                st.session_state.units.append({"name": name, "major": major, "credits": cred})
                # ここに保存処理(save_data)を記述
                st.rerun()
