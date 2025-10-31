import streamlit as st

if "github_api" not in st.session_state:
    st.warning("⚠️ 로그인이 필요합니다.")
    if st.button("🔐 로그인하기"):
        st.switch_page("main.py")
    st.stop()

if "selected_repo" not in st.session_state:
    st.warning("⚠️ 레포지토리를 선택해주세요.")
    if st.button("← 목록으로 돌아가기"):
        st.switch_page("pages/repositories.py")
    st.stop()

github_api = st.session_state.github_api
repo_name = st.session_state.selected_repo

# 뒤로가기 버튼
if st.button("← 레포 목록"):
    st.switch_page("pages/home.py")

st.title(f"📦 {repo_name}")

# PR 목록 가져오기
with st.spinner("PR 목록 불러오는 중..."):
    try:
        pulls = github_api.get_pull_requests(repo_name)
        
        st.subheader(f"Pull Requests ({len(pulls)})")
        
        if pulls:
            for pr in pulls:
                with st.container():
                    col1, col2, col3 = st.columns([0.75, 0.15, 0.1])
                    with col1:
                        st.markdown(f"**#{pr['number']} {pr['title']}**")
                        st.caption(f"👤 {pr['user']} · {pr['state']} · {pr['created_at']}")
                    with col2:
                        if st.button("상세보기", key=f"detail_{pr['number']}", use_container_width=True):
                            st.session_state.selected_pr = pr['number']
                            st.switch_page("pages/pr_detail.py")
                    with col3:
                        st.link_button("🔗", pr['url'])
                    st.divider()
        else:
            st.info("📭 Pull Request가 없습니다.")
            
    except Exception as e:
        st.error(f"❌ 오류: {str(e)}")
