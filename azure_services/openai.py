from openai import AzureOpenAI as OpenAIClient
from . import azure_config
import os

class AzureOpenAI:
    """Azure OpenAI 클라이언트"""
    
    def __init__(self):
        self.client = OpenAIClient(
            api_key=azure_config.openai_key,
            api_version=azure_config.openai_version,
            azure_endpoint=azure_config.openai_endpoint
        )
        self.deployment = azure_config.openai_deployment
        
        # 프롬프트 디렉토리
        self.prompts_dir = os.path.join(os.path.dirname(__file__), '..', 'prompts')
    
    def _load_prompt(self, filename):
        """프롬프트 파일 로드"""
        filepath = os.path.join(self.prompts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def chat(self, messages, temperature=0.3, max_tokens=1000):
        """채팅 완성 요청"""
        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI 호출 실패: {str(e)}")
            return None
    
    def analyze_code(self, code, conventions, file_path=""):
        """코드 분석 (컨벤션 기반)"""
        # 프롬프트 로드 및 변수 치환
        prompt_template = self._load_prompt('code-review.txt')
        
        prompt = prompt_template.format(
            conventions=conventions,
            file_path=file_path,
            code=code
        )
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        return self.chat(messages, temperature=0.3)