import streamlit as st

PINK = "#FF69B4"
WHITE = "#FFFFFF"
STR_FONT = "'Comic Sans MS', 'Baloo', 'Chilanka', 'Quicksand', cursive, sans-serif"
st.set_page_config(page_title="原谅我", page_icon="🍓", layout="centered")

if "not_accept_count" not in st.session_state:
    st.session_state["not_accept_count"] = 0
if "accepted" not in st.session_state:
    st.session_state["accepted"] = False

def on_not_accept():
    st.session_state["not_accept_count"] += 1

def on_accept():
    st.session_state["accepted"] = True

# 展示主页面
if not st.session_state["accepted"]:
    st.markdown(
        f"""
        <div style="background:{WHITE};padding:0;text-align:center;">
            <div style="font-size:72px; margin-top:30px;">🍓</div>
            <div style="color:{PINK}; font-family:{STR_FONT}; font-size:36px; font-weight:bold;">原谅我</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # 计算按钮大小
    n = st.session_state["not_accept_count"]
    max_n = 4
    min_size = 18  # px
    max_size = 38  # px
    if n < max_n:
        # 按钮大小等比缩放
        btn_size = max_size - (max_size-min_size) * n/(max_n-1) if max_n > 1 else min_size
        btn_style = f"""
            font-size: {btn_size}px;
            font-family: {STR_FONT};
            color: {PINK};
            background: {WHITE};
            border-radius: 32px;
            border: 2px solid {PINK};
            font-weight:bold;
            padding: 18px 32px;
            margin: 16px;
            box-shadow: 0 4px 16px #ffd1e7;
            transition: 0.2s;
        """
        accept_size = min_size + (max_size - min_size) * n/(max_n-1) if max_n > 1 else max_size
        accept_btn_style = f"""
            font-size: {accept_size}px;
            font-family: {STR_FONT};
            color: {PINK};
            background: {WHITE};
            border-radius: 32px;
            border: 2px solid {PINK};
            font-weight:bold;
            padding: 18px 32px;
            margin: 16px;
            box-shadow: 0 4px 16px #ffd1e7;
            transition: 0.2s;
        """
        # 三列排布，按钮对称
        c1, c2, c3 = st.columns([1,1,1])
        with c1:
            # 不接受按钮
            if st.button("❌ 不接受", key=f"no{n}", help="点我会变小哦~"):
                on_not_accept()
            st.markdown(
                f"""
                <style>
                div[data-testid="column"]:nth-of-type(1) button {{
                    {btn_style}
                }}
                </style>
                """, unsafe_allow_html=True
            )
        with c2:
            st.write("")  # 空列居中
        with c3:
            # 接受按钮
            if st.button("💗 接受", key=f"yes{n}", help="点我会变大哦~"):
                on_accept()
            st.markdown(
                f"""
                <style>
                div[data-testid="column"]:nth-of-type(3) button {{
                    {accept_btn_style}
                }}
                </style>
                """, unsafe_allow_html=True
            )
    else:
        # 只显示巨大的接受按钮且居中
        big_btn_style = f"""
            font-size: 48px;
            font-family: {STR_FONT};
            color: {PINK};
            background: {WHITE};
            border-radius: 42px;
            border: 3px solid {PINK};
            font-weight:bold;
            padding: 28px 80px;
            margin: 40px 0;
            box-shadow: 0 6px 32px #ffd1e7;
        """
        st.write("")
        st.write("")
        # 居中显示
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("💗 接受", key="onlyyes", help="点我！"):
                on_accept()
            st.markdown(
                f"""
                <style>
                div[data-testid="column"]:nth-of-type(2) button {{
                    {big_btn_style}
                }}
                </style>
                """, unsafe_allow_html=True
            )
else:
    # 太好了页面
    st.markdown(
        f"""
        <div style="background:{WHITE};padding:0;text-align:center;">
            <div style="color:{PINK}; font-family:{STR_FONT}; font-size:88px; font-weight:bold; margin-top:120px;">太好了！</div>
        </div>
        """, unsafe_allow_html=True
    )
