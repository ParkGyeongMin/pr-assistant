import os
from dotenv import load_dotenv

load_dotenv()

class AzureConfig:
    "Azure class setting"
    def __init__(self):
        self.search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT") 
        self.search_key = os.getenv("AZURE_SEARCH_API_KEY") 

        self.openai_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.openai_version = os.getenv("AZURE_OPENAI_API_VERSION")
        self.openai_endpoint = os.getenv("AZURE_OPENAI_API_ENDPOINT")
        self.openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        self.storage_connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


    def get_index_name(self, language):
        """언어별 인덱스 이름 생성"""
        return f"{language.lower()}-code-convention"  # ⭐ 변경
    
    @classmethod
    def validate(cls):
        return True

azure_config = AzureConfig()  # 클래스를 호출해서 인스턴스 만듦

# Export
from .search import AzureSearch
from .openai import AzureOpenAI

__all__ = ['AzureConfig', 'azure_config', 'AzureSearch', 'AzureOpenAI']
