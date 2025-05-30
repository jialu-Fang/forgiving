import streamlit as st

PINK = "#FF69B4"
WHITE = "#FFFFFF"
STR_FONT = "'Comic Sans MS', 'Baloo', 'Chilanka', 'Quicksand', cursive, sans-serif"
st.set_page_config(page_title="原谅我", page_icon="🍓", layout="centered")

if "not_accept_count" not in st.session_state:
    st.session_state["not_accept_count"] = 0
if "accepted" not in st.session_state:
    st.session_state["accepted"] = False

def get_btn_size(n, max_n=4, min_size=18, max_size=38):
    step = (max_size - min_size) / (max_n - 1)
    return max_size - step * n, min_size + step * n

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
    n = st.session_state["not_accept_count"]
    max_n = 4
    min_size = 18
    max_size = 38

    if n < max_n:
        no_size, yes_size = get_btn_size(n, max_n, min_size, max_size)
        btn_style = lambda fs: f"""
            font-size: {fs}px;
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
        c1, c2, c3 = st.columns([1,0.2,1])
        with c1:
            if st.button("❌ 不接受", key=f"no{n}", help="点我会变小哦~", use_container_width=True):
                st.session_state["not_accept_count"] += 1
            st.markdown(
                f"""
                <style>
                div[data-testid="column"]:nth-of-type(1) button {{
                    {btn_style(no_size)}
                }}
                </style>
                """, unsafe_allow_html=True
            )
        with c2:
            pass
        with c3:
            if st.button("💗 接受", key=f"yes{n}", help="点我会变大哦~", use_container_width=True):
                st.session_state["accepted"] = True
            st.markdown(
                f"""
                <style>
                div[data-testid="column"]:nth-of-type(3) button {{
                    {btn_style(yes_size)}
                }}
                </style>
                """, unsafe_allow_html=True
            )
    else:
        big_btn_style = f"""
            font-size: 52px;
            font-family: {STR_FONT};
            color: {PINK};
            background: {WHITE};
            border-radius: 42px;
            border: 3px solid {PINK};
            font-weight:bold;
            padding: 32px 100px;
            margin: 40px 0;
            box-shadow: 0 6px 32px #ffd1e7;
        """
        st.write("")
        st.write("")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("💗 接受", key="onlyyes", help="点我！", use_container_width=True):
                st.session_state["accepted"] = True
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
    st.markdown(
        f"""
        <div style="background:{WHITE};padding:0;text-align:center;">
            <div style="color:{PINK}; font-family:{STR_FONT}; font-size:88px; font-weight:bold; margin-top:120px;">
                太好了！
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
