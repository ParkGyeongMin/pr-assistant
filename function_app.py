import azure.functions as func
import logging
import json
import os
from api.GitHubAPI import GitHubAPI
from service.code_reviewer import CodeReviewer
from azure.data.tables import TableServiceClient

app = func.FunctionApp()

def is_auto_review_enabled():
    """전역 자동 리뷰 설정 확인"""
    try:
        connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        if not connection_string:
            logging.warning("AZURE_STORAGE_CONNECTION_STRING not found")
            return False
        
        table_service = TableServiceClient.from_connection_string(connection_string)
        table_client = table_service.get_table_client('prreviewsettings')
        
        entity = table_client.get_entity(
            partition_key="global",
            row_key="auto_review"
        )
        
        enabled = entity.get('enabled', False)
        logging.info(f"Auto review setting: {enabled}")
        return enabled
    except Exception as e:
        logging.warning(f"Failed to check auto review setting: {e}")
        return False  # 기본값: 비활성화

@app.route(route="pr-review", auth_level=func.AuthLevel.FUNCTION)
def PRReviewTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('PR Review Function triggered')
    
    try:
        if not is_auto_review_enabled():
            logging.info("Auto review is disabled globally")
            return func.HttpResponse("Auto review disabled", status_code=200)
        
        payload = req.get_json()
        
        if payload.get('action') not in ['opened', 'synchronize']:
            logging.info(f"Skipping action: {payload.get('action')}")
            return func.HttpResponse("Not a PR event", status_code=200)
        
        pr_number = payload['pull_request']['number']
        repo_name = payload['repository']['full_name']
        
        logging.info(f"Processing PR #{pr_number} in {repo_name}")
        
        github_api = GitHubAPI(os.getenv('GITHUB_TOKEN'))
        reviewer = CodeReviewer()
        
        files = github_api.get_pull_request_files(repo_name, pr_number)
        logging.info(f"Found {len(files)} files")
        
        reviewed_count = 0
        
        for file in files:
            logging.info(f"Checking file: {file.get('filename')}")
            
            if file.get('patch'):
                logging.info(f"Reviewing {file['filename']}")
                
                review = reviewer.review_code(
                    filename=file['filename'],
                    code_diff=file['patch']
                )
                logging.info(f"Review result preview: {review[:200]}")
                logging.info(f"Issues found! Adding comment to {file['filename']}")
                
                github_api.add_file_comment(
                    repo_name, pr_number,
                    f"## 🤖 AI 자동 리뷰\n\n{review}",
                    file['filename']
                )

                reviewed_count += 1
                logging.info(f"Comment added successfully")
            else:
                logging.info(f"No patch for {file['filename']}")
        
        logging.info(f"Review completed: {reviewed_count} comments added")
        return func.HttpResponse(f"Reviewed {reviewed_count} files", status_code=200)
        
    except Exception as e:
        logging.error(f"Error: {str(e)}", exc_info=True)
        return func.HttpResponse(f"Error: {e}", status_code=500)