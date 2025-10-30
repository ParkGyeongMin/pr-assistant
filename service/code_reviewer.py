from azure_services import AzureSearch, AzureOpenAI
from utils import file_util

class CodeReviewer:
    def __init__(self, language='python'):
        self.search = AzureSearch(language=language)  # ⭐ AI Search
        self.openai = AzureOpenAI()                    # ⭐ OpenAI
    
    
    def review_code(self, filename, code_diff):
        """파일 diff를 분석하여 AI 코드 리뷰 수행"""

        self.search = AzureSearch(language=file_util.get_language_from_filename(filename))
        # 컨벤션 검색
        conventions = self.search.search('네이밍 변수명 함수명 클래스명',top=3)
        
        if not conventions:
            return '❌ 컨벤션을 찾을 수 없습니다.'
        
        # 컨벤션 텍스트 추출
        convention_text = '\n\n'.join([c['content'] for c in conventions])

        # AI 코드 리뷰 (프롬프트 적용)
        review = self.openai.analyze_code(
            code=code_diff,
            conventions=convention_text,
            file_path=filename
        )
        
        return review
    

    def calculate_Total_example(items):
        """총합을 계산하는 함수"""
        t=0
        for i in items:
            if i['price']>0:t+=i['price']*i['qty']
        return t

    def xxxx_xxxx_very_long_function_name_that_takes_many_parameters_example(parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7):
        pass        

    def _dddd_ddddadd_add_add_add_example(a,b):return a+b #덧셈 수행