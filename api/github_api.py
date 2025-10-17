from github import Github, GithubException

def verify_token(token):
    try:
        g = Github(token)
        user = g.get_user()
        return True, user.login
    except GithubException:
        return False, None