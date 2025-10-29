from azure_services import AzureSearch, AzureOpenAI

class CodeReviewer:
    def __init__(self, language="python"):
        self.search = AzureSearch(language=language)  # ⭐ AI Search
        self.openai = AzureOpenAI()                    # ⭐ OpenAI
        
    def review_code(self, filename, patch):
        """파일 diff를 분석하여 AI 코드 리뷰 수행"""
        # 언어 판단
        # language = filename.split('.')[-1] if '.' in filename else 'python'
        self.search = AzureSearch(language="python")
        
        # 컨벤션 검색
        conventions = self.search.search("네이밍 변수명 함수명 클래스명", top=3)
        
        if not conventions:
            return "❌ 컨벤션을 찾을 수 없습니다."
        
        # 컨벤션 텍스트 추출
        convention_text = "\n\n".join([c['content'] for c in conventions])
        
        # AI 코드 리뷰 (프롬프트 적용)
        review = self.openai.analyze_code(
            code=patch,
            conventions=convention_text,
            file_path=filename
        )
        
        return review