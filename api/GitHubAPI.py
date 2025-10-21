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