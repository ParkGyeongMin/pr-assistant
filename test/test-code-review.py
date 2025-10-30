"""코드 리뷰 테스트"""
import sys
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

print(f"프로젝트 루트: {project_root}")
print(f"azure_services 존재: {(project_root / 'azure_services').exists()}")


from azure_services import AzureSearch, AzureOpenAI

# 1. 클라이언트 생성
print("=== Azure 클라이언트 초기화 ===")
search = AzureSearch(language="python")
openai = AzureOpenAI()
print("✅ 초기화 완료\n")

# 2. 테스트할 코드 (일부러 컨벤션 위반)
test_code = """
+from azure_services import AzureSearch, AzureOpenAI
+
+class CodeReviewer:
+    def __init__(self, language='python'):
+        self.search = AzureSearch(language=language)  # ⭐ AI Search
+        self.openai = AzureOpenAI()                    # ⭐ OpenAI
+        
+    def review_code(self, filename, code_diff):
+
+        # language = filename.split('.')[-1] if '.' in filename else 'python'
+        self.search = AzureSearch(language='python')
+        
+        # 컨벤션 검색
+        conventions = self.search.search('네이밍 변수명 함수명 클래스명',top=3)
+        
+        if not conventions:
+            return '❌ 컨벤션을 찾을 수 없습니다.'
+        
+        # 컨벤션 텍스트 추출
+        convention_text = '\n\n'.join([c['content'] for c in conventions])
+        
+        # AI 코드 리뷰 (프롬프트 적용)
+        review_result = self.openai.analyze_code(
+            code=code_diff,
+            conventions=convention_text,
+            file_path=filename
+        )
+        
+        return review_result
"""
# 3. AI Search에서 컨벤션 검색
print("=== 컨벤션 검색 중... ===")
conventions = search.search("네이밍 변수명 함수명 클래스명", top=3)

if conventions:
    print(f"✅ {len(conventions)}개 컨벤션 발견")
    for i, conv in enumerate(conventions, 1):
        print(f"{i}. {conv['title']} (점수: {conv['score']:.2f})")
else:
    print("❌ 컨벤션을 찾을 수 없습니다.")
    exit()

print()

# 4. 컨벤션 텍스트 추출
convention_text = "\n\n".join([c['content'] for c in conventions])
print("=== 적용할 컨벤션 (일부) ===")
print(convention_text[:300] + "...\n")

# 5. AI 코드 리뷰
print("=== AI 코드 리뷰 중... ===")
review = openai.analyze_code(
    code=test_code,
    conventions=convention_text,
    file_path="test.py"
)

print("=== 리뷰 결과 ===")
print(review)