import streamlit as st
import time

st.set_page_config(page_title="PR Assistant", layout="wide")

# 세션 초기화
if "github_token" not in st.session_state:
    st.session_state.github_token = None
if "ai_loaded" not in st.session_state:
    st.session_state.ai_loaded = False

st.title("PR Assistant")
st.write("🤖 AI 모델 로딩 및 인증")

# AI 로딩
with st.spinner("AI 모델을 로딩하는 중..."):
    if not st.session_state.ai_loaded:
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.03)  # 3초
            progress_bar.progress(i + 1)
        st.session_state.ai_loaded = True
        st.success("✅ AI 모델 로딩 완료!")

# Token 입력
st.subheader("GitHub 인증")
token = st.text_input("GitHub Personal Access Token", type="password", 
                      placeholder="ghp_xxxxxxxxxxxx")

if st.button("로그인", type="primary"):
    if token:
        st.session_state.github_token = token
        st.success("✅ 인증 성공!")
        time.sleep(1)
        st.switch_page("pages/home.py")
    else:
        st.error("❌ Token을 입력해주세요.")