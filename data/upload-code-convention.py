# upload_conventions.py
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

import os
from dotenv import load_dotenv
import uuid

load_dotenv()

# 클라이언트 생성
client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="python-code-convention",  # 인덱스명
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
)

# Markdown 읽기
with open('data/python-code-convention.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 업로드
doc = [{
    "id": str(uuid.uuid4()),
    "title": "Python 코드 컨벤션",
    "content": content,
    "category": "general",
    "language": "python"
}]

result = client.upload_documents(documents=doc)
print("✅ 업로드 완료!")