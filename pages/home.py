import streamlit as st


if "github_api" not in st.session_state:
    st.warning("⚠️ 로그인이 필요합니다.")
    st.markdown("GitHub 레포지토리를 확인하려면 먼저 로그인해주세요.")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔐 로그인하기", use_container_width=True, type="primary"):
            st.switch_page("main.py")
    st.stop()

github_api = st.session_state.github_api

st.title("Repository 목록")
st.write(f"환영합니다")

# 필터 생성
filters = [
    {"type": "all", "label": "All (전체)"},
    {"type": "my", "label": "My Repo"}
]

# 조직 추가
orgs = github_api.get_organizations()
for org in orgs:
    filters.append({"type": "organization", "label": f"{org} 조직", "org": org})

# 초대받은 레포 그룹화 추가
collab_grouped = github_api.get_collaborator_repositories_grouped()
for owner_key, repo_list in collab_grouped.items():
    filters.append({
        "type": "collaborator_owner",
        "label": f"👤 {owner_key} (초대)",
        "repos": repo_list
    })

# 필터 선택
filter_labels = [f["label"] for f in filters]
selected_label = st.selectbox("📂 레포 필터", filter_labels)

# 선택된 필터 찾기
selected_filter = next(f for f in filters if f["label"] == selected_label)

# 레포지토리 목록 가져오기
with st.spinner("레포지토리 불러오는 중..."):
    try:
        # 필터에 따라 레포 가져오기
        if selected_filter["type"] == "all":
            repos = github_api.get_all_repositories()
        elif selected_filter["type"] == "my":
            repos = github_api.get_my_repositories()
        elif selected_filter["type"] == "collaborator":
            repos = github_api.get_collaborator_repositories()
        elif selected_filter["type"] == "organization":
            repos = github_api.get_organization_repositories(selected_filter["org"])
        elif selected_filter["type"] == "collaborator_owner":
            repos = selected_filter["repos"]
        
        if repos:
            # 상단 정보 및 필터
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.metric("총 레포지토리", len(repos))
            with col2:
                search = st.text_input("🔍", placeholder="검색...", label_visibility="collapsed", key="search_input")   
            with col3:
                view_mode = st.selectbox("보기", ["목록", "그리드"], label_visibility="collapsed")
            
            st.divider()
            
            # 필터링
            filtered_repos = [
                repo for repo in repos 
                if search.lower() in repo.lower()
            ] if search else repos
            
            
            # 레포지토리 표시
            if filtered_repos:
                if view_mode == "목록":
                    # 목록 보기
                    for i, repo in enumerate(filtered_repos, 1):
                        with st.container():
                            col1, col2 = st.columns([0.85, 0.15])
                            with col1:
                                st.markdown(f"**{i}. {repo}**")
                            with col2:
                                if st.button("열기", key=f"grid_{i}", use_container_width=True):
                                    st.session_state.selected_repo = repo
                                    st.switch_page("pages/repository_detail.py")
                            st.divider()
                else:
                    # 그리드 보기
                    cols = st.columns(3)
                    for i, repo in enumerate(filtered_repos):
                        with cols[i % 3]:
                            with st.container():
                                st.markdown(f"#### 📦 {repo.split('/')[-1]}")
                                if '/' in repo:
                                    st.caption(f"👤 {repo.split('/')[0]}")
                                if st.button("열기", key=f"open_{i}", use_container_width=True):
                                    st.session_state.selected_repo = repo
                                    st.switch_page("pages/repository_detail.py")
            else:
                st.warning(f"'{search}'와 일치하는 레포지토리가 없습니다.")
        else:
            st.info("📭 레포지토리가 없습니다.")
            st.markdown("새 레포지토리를 만들어보세요!")
            
    except Exception as e:
        st.error(f"❌ 오류: {str(e)}")
        if st.button("🔄 다시 시도"):
            st.rerun()