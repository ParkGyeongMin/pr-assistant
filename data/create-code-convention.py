# create_index.py
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchFieldDataType
)
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()

# 인덱스 클라이언트
index_client = SearchIndexClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
)

# 필드 정의
fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="title", type=SearchFieldDataType.String),
    SearchableField(name="content", type=SearchFieldDataType.String),
    SimpleField(name="category", type=SearchFieldDataType.String, filterable=True),
    SimpleField(name="language", type=SearchFieldDataType.String, filterable=True)
]

# 인덱스 생성
index = SearchIndex(name="python-code-convention", fields=fields)

try:
    result = index_client.create_index(index)
    print(f"✅ 인덱스 '{result.name}' 생성 완료!")
except Exception as e:
    print(f"❌ 오류: {e}")