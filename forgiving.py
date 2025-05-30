import streamlit as st

# 配色和字体
PINK = "#FF69B4"
LIGHT_PINK = "#FFB6C1"
WHITE = "#FFFFFF"
STR_FONT = "'Comic Sans MS', 'Baloo', 'Chilanka', 'Quicksand', cursive, sans-serif"
st.set_page_config(page_title="原谅我", page_icon="🍓", layout="centered", initial_sidebar_state="collapsed")

# Session State 初始化
if 'not_accept_count' not in st.session_state:
    st.session_state['not_accept_count'] = 0
if 'accepted' not in st.session_state:
    st.session_state['accepted'] = False

def not_accept():
    st.session_state['not_accept_count'] += 1

def accept():
    st.session_state['accepted'] = True

# 自定义可爱按钮的CSS
st.markdown(
    f"""
    <style>
    .cute-btn {{
        display: inline-block;
        padding: 16px 48px;
        font-size: 28px;
        font-weight: bold;
        color: {WHITE};
        background: linear-gradient(90deg, {PINK} 30%, {LIGHT_PINK} 100%);
        border: none;
        border-radius: 32px;
        box-shadow: 0 4px 24px #ffd1e7;
        cursor: pointer;
        transition: all 0.2s;
        margin: 12px 20px;
        font-family: {STR_FONT};
        letter-spacing: 2px;
    }}
    .cute-btn:hover {{
        background: linear-gradient(90deg, {LIGHT_PINK} 30%, {PINK} 100%);
        color: {PINK};
        border: 2px solid {PINK};
        box-shadow: 0 6px 32px {LIGHT_PINK};
        transform: scale(1.07);
    }}
    /* 隐藏原生 stButton */
    div.stButton > button {{
        display: none;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 主界面
st.markdown(
    f"""
    <div style="background:{WHITE};padding:0;border-radius:20px;text-align:center;">
        <div style="font-size:72px; margin-top:30px;">🍓</div>
        <div style="color:{PINK}; font-family:{STR_FONT}; font-size:36px; font-weight:bold;">原谅我</div>
    </div>
    """, unsafe_allow_html=True
)

if not st.session_state['accepted']:
    # 按钮区
    c1, c2, c3 = st.columns([1,2,1])
    with c1:
        if st.session_state['not_accept_count'] < 4:
            scale = 28 - 4 * st.session_state['not_accept_count']
            st.markdown(
                f"""<button class="cute-btn" style="font-size:{scale}px" onclick="window.parent.postMessage({{btn:'notaccept'}}, '*')">❌ 不接受</button>""",
                unsafe_allow_html=True,
            )
    with c2:
        accept_scale = 28 + 6 * st.session_state['not_accept_count'] if st.session_state['not_accept_count'] < 4 else 48
        btn_html = f"""<button class="cute-btn" style="font-size:{accept_scale}px" onclick="window.parent.postMessage({{btn:'accept'}}, '*')">💗 接受</button>"""
        st.markdown(btn_html, unsafe_allow_html=True)

    # Streamlit 事件监听（交互适配）
    st.markdown("""
    <script>
    // 只添加一次事件监听
    if (!window.buttonListenerAdded) {
        window.addEventListener('message', function(event) {
            if (event.data && event.data.btn === 'notaccept') {
                window.parent.postMessage({streamlitSetComponentValue: {key: "notaccept", value: true}}, '*');
            }
            if (event.data && event.data.btn === 'accept') {
                window.parent.postMessage({streamlitSetComponentValue: {key: "accept", value: true}}, '*');
            }
        }, false);
        window.buttonListenerAdded = true;
    }
    </script>
    """, unsafe_allow_html=True)

    # 使用 Streamlit 的隐藏按钮来触发事件
    notaccept = st.button("notaccept", key="btn_notaccept")
    acceptbtn = st.button("accept", key="btn_accept")
    # 通过 session_state 响应 html 按钮
    if st.session_state.get("notaccept", False):
        not_accept()
        st.session_state["notaccept"] = False
        st.experimental_rerun()
    if st.session_state.get("accept", False):
        accept()
        st.session_state["accept"] = False
        st.experimental_rerun()

else:
    st.markdown(
        f"""
        <div style="background:{WHITE};padding:0;text-align:center;">
            <div style="color:{PINK}; font-family:{STR_FONT}; font-size:72px; font-weight:bold; margin-top:80px;">太好了！</div>
        </div>
        """, unsafe_allow_html=True
    )
