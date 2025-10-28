from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from . import azure_config

class AzureSearch:
    """Azure AI Search 클라이언트"""
    
    def __init__(self, language="python"):
        self.config = azure_config
        self.index_name = self.config.get_index_name(language)
        
        self.search_client = SearchClient(
            endpoint=self.config.search_endpoint,
            index_name=self.index_name,
            credential=AzureKeyCredential(self.config.search_key)
        )
    
    def search(self, query, top=3, filter_category=None):
        """문서 검색"""
        try:
            filter_expr = f"category eq '{filter_category}'" if filter_category else None
            
            results = self.search_client.search(
                search_text=query,
                top=top,
                filter=filter_expr,
                select=["title", "content", "category"]
            )
            
            documents = []
            for result in results:
                documents.append({
                    "title": result.get("title"),
                    "content": result.get("content"),
                    "category": result.get("category"),
                    "score": result.get("@search.score")
                })
            
            return documents
            
        except Exception as e:
            print(f"검색 실패: {str(e)}")
            return []