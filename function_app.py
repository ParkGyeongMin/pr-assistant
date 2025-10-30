import azure.functions as func
import logging
import json
import os
from api.GitHubAPI import GitHubAPI
from service.code_reviewer import CodeReviewer

app = func.FunctionApp()

@app.route(route="pr-review", auth_level=func.AuthLevel.FUNCTION)
def PRReviewTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('PR Review Function triggered')
    
    try:
        payload = req.get_json()
        logging.info(f"Payload: {payload}")

        # PR 이벤트 확인
        if payload.get('action') not in ['opened', 'synchronize']:
            return func.HttpResponse("Not a PR event", status_code=200)
        
        # PR 정보
        pr_number = payload['pull_request']['number']
        repo_name = payload['repository']['full_name']
        
        logging.info(f"Reviewing PR #{pr_number}")
        
        # GitHub API 초기화
        github_api = GitHubAPI(os.getenv('GITHUB_TOKEN'))
        reviewer = CodeReviewer()
        
        # PR 파일들 가져오기
        files = github_api.get_pull_request_files(repo_name, pr_number)
        
        for file in files:
            if file.get('patch'):
                # 리뷰 수행
                review = reviewer.review_code(
                    filename=file['filename'],
                    code_diff=file['patch']
                )
                
                # 문제 발견 시 코멘트
                if '❌' in review:
                    github_api.add_file_comment(
                        repo_name, pr_number,
                        f"## 🤖 AI 리뷰\n\n{review}",
                        file['filename']
                    )
        
        return func.HttpResponse("Review completed", status_code=200)
        
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {e}", status_code=500)