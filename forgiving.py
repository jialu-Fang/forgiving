import streamlit as st

# 配色和字体
PINK = "#FF69B4"
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
    c1, c2, c3 = st.columns([1,2,1])
    with c1:
        if st.session_state['not_accept_count'] < 4:
            # 不接受按钮，变小
            scale = 24 - 4 * st.session_state['not_accept_count']
            st.button(
                "不接受",
                key="notaccept",
                on_click=not_accept,
                help="点击我试试看",
                use_container_width=True
            )
            st.markdown(
                f"<style>div[data-testid='stButton'] button#notaccept {{font-size:{scale}px;color:{PINK};background:{WHITE};border:2px solid {PINK};border-radius:20px;}}</style>",
                unsafe_allow_html=True
            )
    with c2:
        # 接受按钮，变大
        accept_scale = 24 + 6 * st.session_state['not_accept_count'] if st.session_state['not_accept_count'] < 4 else 48
        st.button(
            "接受",
            key="accept",
            on_click=accept,
            use_container_width=True
        )
        st.markdown(
            f"<style>div[data-testid='stButton'] button#accept {{font-size:{accept_scale}px;color:{PINK};background:{WHITE};border:2px solid {PINK};border-radius:20px;}}</style>",
            unsafe_allow_html=True
        )
else:
    st.markdown(
        f"""
        <div style="background:{WHITE};padding:0;text-align:center;">
            <div style="color:{PINK}; font-family:{STR_FONT}; font-size:72px; font-weight:bold; margin-top:80px;">太好了！</div>
        </div>
        """, unsafe_allow_html=True
    )
