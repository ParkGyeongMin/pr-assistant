from github import Github, GithubException

class GitHubAPI:
    def __init__(self, token):
        self.github = Github(token)
        self.user = None
    
    def verify_token(self):
        try:
            self.user = self.github.get_user()

            return True, self.user.login
        except GithubException:
            return False, None
    
    def get_username(self):
        """사용자 이름 반환"""
        if self.user:
            return self.user.login
        return None
    
    def get_all_repositories(self):
        """모든 레포지토리"""
        if not self.user:
            self.user = self.github.get_user()
        repos = self.user.get_repos()
        return [repo.full_name for repo in repos]
    
    def get_my_repositories(self):
        """내 개인 레포만"""
        if not self.user:
            self.user = self.github.get_user()
        repos = self.user.get_repos(affiliation='owner')
        return [repo.full_name for repo in repos]
    
    def get_collaborator_repositories(self):
        """초대받은 레포 전체"""
        if not self.user:
            self.user = self.github.get_user()
        repos = self.user.get_repos(affiliation='collaborator')
        return [repo.full_name for repo in repos]
    
    def get_organizations(self):
        """소속된 조직 목록"""
        if not self.user:
            self.user = self.github.get_user()
        orgs = self.user.get_orgs()
        return [org.login for org in orgs]
    
    def get_organization_repositories(self, org_name):
        """특정 조직의 레포"""
        org = self.github.get_organization(org_name)
        repos = org.get_repos()
        return [repo.full_name for repo in repos]
    
    def get_collaborator_repositories_grouped(self):
        """초대받은 레포를 소유자 타입별로 그룹화"""
        if not self.user:
            self.user = self.github.get_user()
        repos = self.user.get_repos(affiliation='collaborator')
        
        grouped = {}
        for repo in repos:
            owner_name = repo.owner.login
            owner_type = repo.owner.type
            
            key = f"{owner_name} ({'조직' if owner_type == 'Organization' else '개인'})"
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(repo.full_name)
        
        return grouped
    
    def get_pull_requests(self, repo_name):
        """main 브랜치로 들어오는 PR 목록"""
        repo = self.github.get_repo(repo_name)
        pulls = repo.get_pulls(state='all', base='main')
        
        return [
            {
                'number': pr.number,
                'title': pr.title,
                'state': pr.state,
                'user': pr.user.login,
                'created_at': pr.created_at.strftime('%Y-%m-%d'),
                'url': pr.html_url
            }
            for pr in pulls
        ]
    
    def get_pull_request_detail(self, repo_name, pr_number):
        """PR 상세 정보 가져오기"""
        repo = self.github.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        
        return {
            'number': pr.number,
            'title': pr.title,
            'body': pr.body,
            'state': pr.state,
            'user': pr.user.login,
            'created_at': pr.created_at.strftime('%Y-%m-%d %H:%M'),
            'commits': pr.commits,
            'changed_files': pr.changed_files,
            'additions': pr.additions,
            'deletions': pr.deletions,
            'url': pr.html_url
        }
    
    def get_pull_request_files(self, repo_name, pr_number):
        """PR의 변경된 파일 목록"""
        repo = self.github.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        files = pr.get_files()
        
        return [
            {
                'filename': file.filename,
                'status': file.status,
                'additions': file.additions,
                'deletions': file.deletions,
                'changes': file.changes,
                'patch': file.patch if hasattr(file, 'patch') else None
            }
            for file in files
    ]

    def get_pull_request_commits(self, repo_name, pr_number):
        """PR의 커밋 목록"""
        repo = self.github.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        commits = pr.get_commits()
        
        return [
            {
                'sha': commit.sha[:7],
                'message': commit.commit.message,
                'author': commit.commit.author.name,
                'date': commit.commit.author.date.strftime('%Y-%m-%d %H:%M')
            }
            for commit in commits
        ]

    def get_pull_request_comments(self, repo_name, pr_number):
        """PR의 코멘트"""
        repo = self.github.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        
        comments = []
        
        # Issue 코멘트
        for comment in pr.get_issue_comments():
            comments.append({
                'type': 'comment',
                'user': comment.user.login,
                'body': comment.body,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
            })
        
        # 리뷰 코멘트
        for comment in pr.get_review_comments():
            comments.append({
                'type': 'review',
                'user': comment.user.login,
                'body': comment.body,
                'path': comment.path,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
            })
        
        return sorted(comments, key=lambda x: x['created_at'])
    
    def add_commit_comment(self, repo_name, commit_sha, body):
        """커밋에 코멘트 추가"""
        repo = self.github.get_repo(repo_name)
        commit = repo.get_commit(commit_sha)
        commit.create_comment(body)

    def add_file_comment(self, repo_name, pr_number, body, path, line):
        """파일 특정 라인에 코멘트 추가"""
        repo = self.github.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        pr.create_review_comment(body, repo.get_commit(pr.head.sha), path, line)

    def add_pr_comment(self, repo_name, pr_number, body):
        """PR 전체에 코멘트 추가"""
        repo = self.github.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        pr.create_issue_comment(body) 

    def merge_pull_request(self, repo_name, pr_number, merge_method='merge'):
        """PR 병합
        merge_method: 'merge', 'squash', 'rebase'
        """
        repo = self.github.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        
        result = pr.merge(merge_method=merge_method)
        return result.merged