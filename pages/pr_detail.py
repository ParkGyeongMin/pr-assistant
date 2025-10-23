import streamlit as st

if "github_api" not in st.session_state:
    st.warning("⚠️ 로그인이 필요합니다.")
    if st.button("🔐 로그인하기"):
        st.switch_page("main.py")
    st.stop()

if "selected_repo" not in st.session_state or "selected_pr" not in st.session_state:
    st.warning("⚠️ PR을 선택해주세요.")
    if st.button("← 레포 목록으로"):
        st.switch_page("pages/repositories.py")
    st.stop()

github_api = st.session_state.github_api
repo_name = st.session_state.selected_repo
pr_number = st.session_state.selected_pr

# 뒤로가기 버튼
if st.button("← PR 목록"):
    st.switch_page("pages/repository_detail.py")

# PR 상세 정보 가져오기
with st.spinner("PR 정보 불러오는 중..."):
    try:
        pr_detail = github_api.get_pull_request_detail(repo_name, pr_number)
        
        # PR이 Open 상태일 때만 병합 버튼 표시
        if pr_detail['state'] == 'open':
            st.divider()
            st.subheader("🔀 Pull Request 병합")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("✅ Create a merge commit", use_container_width=True):
                    try:
                        if github_api.merge_pull_request(repo_name, pr_number, 'merge'):
                            st.success("✅ 병합 완료!")
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ 오류: {str(e)}")
            
            with col2:
                if st.button("📦 Squash and merge", use_container_width=True):
                    try:
                        if github_api.merge_pull_request(repo_name, pr_number, 'squash'):
                            st.success("✅ 병합 완료!")
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ 오류: {str(e)}")
            
            with col3:
                if st.button("🔄 Rebase and merge", use_container_width=True):
                    try:
                        if github_api.merge_pull_request(repo_name, pr_number, 'rebase'):
                            st.success("✅ 병합 완료!")
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ 오류: {str(e)}")
        
        st.divider()
        
        # PR 정보
        st.title(f"Pull Request #{pr_number}")
        st.subheader(pr_detail['title'])
        st.caption(f"👤 {pr_detail['user']} · {pr_detail['state']} · {pr_detail['created_at']}")
        
        if pr_detail['body']:
            st.markdown("### 설명")
            st.markdown(pr_detail['body'])
        
        st.divider()
        
        # 변경 통계
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("커밋", pr_detail['commits'])
        with col2:
            st.metric("변경 파일", pr_detail['changed_files'])
        with col3:
            st.metric("+/- 라인", f"+{pr_detail['additions']} / -{pr_detail['deletions']}")
        
        st.divider()
        
        # 탭으로 정보 분리
        tab1, tab2, tab3, tab4 = st.tabs(["📝 커밋", "📄 변경 파일", "💬 코멘트", "✍️ 전체 코멘트 작성"])
        
        # 커밋 목록
        with tab1:
            commits = github_api.get_pull_request_commits(repo_name, pr_number)
            if commits:
                for i, commit in enumerate(commits):
                    with st.container():
                        col1, col2 = st.columns([0.85, 0.15])
                        with col1:
                            st.markdown(f"**`{commit['sha']}`** {commit['message'].split(chr(10))[0]}")
                            st.caption(f"👤 {commit['author']} · {commit['date']}")
                        with col2:
                            if st.button("💬", key=f"commit_comment_{i}", use_container_width=True):
                                st.session_state[f"show_commit_input_{i}"] = not st.session_state.get(f"show_commit_input_{i}", False)
                        
                        # 코멘트 입력창
                        if st.session_state.get(f"show_commit_input_{i}", False):
                            comment_text = st.text_area("코멘트 작성", key=f"commit_text_{i}", height=100)
                            if st.button("작성", key=f"commit_submit_{i}"):
                                if comment_text:
                                    try:
                                        github_api.add_commit_comment(repo_name, commit['sha'], comment_text)
                                        st.success("✅ 코멘트가 작성되었습니다!")
                                        st.session_state[f"show_commit_input_{i}"] = False
                                        st.rerun()
                                    except Exception as e:
                                        st.error(f"❌ 오류: {str(e)}")
                        
                        st.divider()
            else:
                st.info("커밋이 없습니다.")
        
        # 변경 파일
        with tab2:
            files = github_api.get_pull_request_files(repo_name, pr_number)
            if files:
                for i, file in enumerate(files):
                    with st.expander(f"📄 {file['filename']} (+{file['additions']} / -{file['deletions']})"):
                        st.caption(f"상태: {file['status']}")
                        
                        col1, col2 = st.columns([0.85, 0.15])
                        with col2:
                            if st.button("💬 파일에 코멘트", key=f"file_comment_btn_{i}", use_container_width=True):
                                st.session_state[f"show_file_input_{i}"] = not st.session_state.get(f"show_file_input_{i}", False)
                        
                        # 파일 코멘트 입력창
                        if st.session_state.get(f"show_file_input_{i}", False):
                            file_comment_text = st.text_area("파일 전체에 대한 코멘트", key=f"file_text_{i}", height=100)
                            line_number = st.number_input("라인 번호 (선택)", min_value=1, key=f"line_num_{i}", value=1)
                            if st.button("작성", key=f"file_submit_{i}"):
                                if file_comment_text:
                                    try:
                                        github_api.add_file_comment(repo_name, pr_number, file_comment_text, file['filename'], line_number)
                                        st.success("✅ 코멘트가 작성되었습니다!")
                                        st.session_state[f"show_file_input_{i}"] = False
                                        st.rerun()
                                    except Exception as e:
                                        st.error(f"❌ 오류: {str(e)}")
                        
                        if file['patch']:
                            st.code(file['patch'], language='diff')
                        else:
                            st.info("변경 내용을 표시할 수 없습니다.")
            else:
                st.info("변경된 파일이 없습니다.")
        
        # 코멘트 목록
        with tab3:
            comments = github_api.get_pull_request_comments(repo_name, pr_number)
            if comments:
                for comment in comments:
                    with st.container():
                        col1, col2 = st.columns([0.85, 0.15])
                        with col1:
                            st.markdown(f"**👤 {comment['user']}**")
                            if comment['type'] == 'review' and 'path' in comment:
                                st.caption(f"📁 {comment['path']}")
                        with col2:
                            st.caption(comment['created_at'])
                        st.markdown(comment['body'])
                        st.divider()
            else:
                st.info("코멘트가 없습니다.")
        
        # 전체 코멘트 작성
        with tab4:
            st.markdown("### PR 전체에 대한 코멘트 작성")
            pr_comment = st.text_area("코멘트를 작성하세요", height=150, key="pr_comment_text")
            if st.button("💬 코멘트 작성", type="primary"):
                if pr_comment:
                    try:
                        github_api.add_pr_comment(repo_name, pr_number, pr_comment)
                        st.success("✅ 코멘트가 작성되었습니다!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ 오류: {str(e)}")
        
    except Exception as e:
        st.error(f"❌ 오류: {str(e)}")