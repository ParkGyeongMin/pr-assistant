import streamlit as st

# 인증 확인
if "github_token" not in st.session_state or not st.session_state.github_token:
    st.warning("⚠️ 로그인이 필요합니다.")
    st.switch_page("main.py")
    st.stop()

st.title("🏠 Home")
st.write("PR Assistant 메인 화면입니다.")

# 로그아웃 버튼
if st.button("🚪 로그아웃"):
    st.session_state.github_token = None
    st.session_state.ai_loaded = False
    st.rerun()