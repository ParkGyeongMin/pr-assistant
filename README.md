# 🚀 PR-Assistant

> AI 기반 코드 리뷰 도우미 - GitHub 사용이 어려운 관리자와 리뷰어를 위한 스마트 솔루션



## 💡 프로젝트 소개

개발자들은 Git/GitHub 사용에 익숙하지만, **코드 리뷰어나 관리자의 경우 GitHub 인터페이스 사용이 미숙**하여 효율적인 코드 리뷰에 어려움을 겪는 경우가 많습니다.

**PR-Assistant**는 이러한 문제를 해결하기 위해 직관적인 웹 인터페이스와 AI 기술을 결합하여 누구나 쉽게 코드 리뷰를 작성하고 관리할 수 있도록 지원하는 솔루션입니다.

### 🎯 핵심 가치

- **접근성**: GitHub에 익숙하지 않아도 누구나 쉽게 코드 리뷰 가능
- **효율성**: AI가 리뷰 초안을 자동 생성하여 시간 절약
- **품질**: 일관된 코드 리뷰 기준 적용으로 코드 품질 향상
- **자동화**: 출장/휴가 중에도 AI가 자동으로 초기 리뷰 진행

## 🌐 데모

**Live Demo**: [https://your-app-url.streamlit.app](https://your-app-url.streamlit.app)

> 💡 GitHub Personal Access Token으로 로그인하여 바로 사용해보실 수 있습니다.

## ✨ 주요 기능

### 🤖 AI 기반 코드 리뷰 생성
- Pull Request의 코드 변경사항을 AI가 자동 분석
- 잠재적 버그, 코드 품질 개선 사항 자동 제안
- 코드 컨벤션 및 API 설계 문서 기반 리뷰

### 🖥️ 사용자 친화적 웹 인터페이스
- GitHub에 익숙하지 않은 사용자도 쉽게 사용 가능한 직관적인 UI
- PR 목록 조회 및 코드 변경사항 확인
- 커밋별, 파일별 상세 리뷰 작성 지원
- PR 병합(Merge) 기능 제공 (merge/squash/rebase)

### ⚙️ 자동화된 리뷰 프로세스
- **수동 모드**: Streamlit UI에서 버튼 클릭으로 AI 리뷰 요청
- **자동 모드**: PR 생성 시 Azure Function이 자동으로 AI 리뷰 실행
- 설정 페이지에서 자동 리뷰 ON/OFF 제어 가능

### ✅ 관리자 검토 및 승인 프로세스
- AI가 생성한 리뷰를 관리자가 검토하고 수정 가능
- 승인 후 GitHub에 자동으로 리뷰 등록

### 🔗 GitHub 완벽 통합
- GitHub API를 통한 양방향 연동
- 리뷰 결과 자동 반영
- 내가 리뷰해야 할 PR 필터링 기능

## 🏗️ 기술 스택

### Frontend
- **Streamlit**: 웹 인터페이스 구현
- **Python**: 백엔드 로직

### GitHub Integration
- **PyGithub**: GitHub API 연동
- **GitHub Webhooks**: PR 생성 이벤트 자동 감지 (예정)

### Azure Services
- **Azure OpenAI (GPT-4.1-mini)**: 코드 분석 및 리뷰 생성
- **Azure AI Search**: 코드 컨벤션 및 API 문서 검색
- **Azure Function**: 자동 리뷰 트리거 및 처리
- **Azure Storage Account**: 자동 리뷰 설정 및 상태 관리


## 📖 사용 흐름

### 수동 리뷰 모드
1. **PR-Assistant 웹페이지 접속**
2. **GitHub 저장소 연동 및 PR 목록 확인**
3. **리뷰할 PR 선택**
4. **🤖 AI 리뷰 요청 버튼 클릭**
5. **AI가 코드 컨벤션 기반 리뷰 생성**
6. **관리자가 리뷰 내용 검토 및 수정**
7. **GitHub에 리뷰 등록** ✅

### 자동 리뷰 모드
1. **팀원이 PR 생성**
2. **Azure Function이 자동 트리거**
3. **AI가 자동으로 초기 리뷰 작성**
4. **관리자가 복귀 후 최종 확인**

## 🎯 기대 효과

### 🔓 접근성 향상
GitHub 사용 경험이 부족한 리뷰어도 쉽게 코드 리뷰에 참여 가능

### ⚡ 생산성 증대
AI 기반 초안 생성으로 리뷰 작성 시간 단축

### 📈 리뷰 품질 개선
- AI의 일관된 분석으로 누락 가능성 있는 이슈 사전 발견
- 코드 컨벤션 준수 여부 자동 확인
- API 설계 문서 기준 검증

### 🏖️ 업무 연속성 보장
출장/휴가 중에도 팀원이 빠른 피드백 받을 수 있음

## 🚀 시작하기

### 사전 요구사항
- Python 3.8 이상
- GitHub Personal Access Token
- Azure OpenAI API Key
- Azure AI Search 서비스

### 환경 설정

1. **저장소 클론**
```bash
git clone url
cd pr-assistant
```

2. **필요한 패키지 설치**
```bash
pip install -r requirements.txt
```

3. **환경 변수 설정**

`.env` 파일을 프로젝트 루트에 생성하고 다음 내용을 설정하세요:
```env
# GitHub 설정
GITHUB_TOKEN=ghp_your_github_personal_access_token

# Azure OpenAI 설정
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_API_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4
AZURE_OPENAI_API_VERSION =your-aip-version

# Azure AI Search 설정
AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
AZURE_SEARCH_API_KEY=your_search_api_key

# Azure Function 설정 (자동 리뷰용)
AZURE_FUNCTION_URL=https://your-function-app.azurewebsites.net/api/review
AZURE_FUNCTION_KEY=your_function_key

AZURE_STORAGE_KEY=your-storage_key
AZURE_STORAGE_CONNECTION_STRING=your-storage_connection_string
```

### API 키 발급 방법

#### GitHub Personal Access Token
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token" 클릭
3. 필요한 권한 선택: `repo`, `read:user`, `write:discussion`
4. 생성된 토큰 복사

#### Azure OpenAI API Key
1. Azure Portal → Azure OpenAI Service
2. "Keys and Endpoint" 메뉴에서 키 확인
3. Deployment에서 모델 이름 확인

#### Azure AI Search API Key
1. Azure Portal → Azure AI Search
2. "Keys" 메뉴에서 Admin Key 확인
3. Index 이름은 직접 생성한 인덱스명 입력

#### Azure Function 생성
1. Azure Portal → "Function App" 검색
2. "만들기" 클릭
3. 기본 설정:
   - **런타임 스택**: Python 3.9 이상
   - **지역**: Korea Central
4. 생성 후 배포 완료 대기

#### Function URL 및 Key 확인
1. Azure Portal → 생성한 Function App
2. "Functions" → 배포된 함수 선택
3. "Function 키 가져오기" 클릭하여 Function URL과 Key 확인
```
   https://your-function-app.azurewebsites.net/api/pr-review-trigger?code=your_function_key
```
### GitHub Webhook 등록
1. **Repository 설정**
   - GitHub Repository → Settings → Webhooks → "Add webhook"

2. **Webhook 설정**
   - **Payload URL**: Azure Function URL 입력 (Key 포함)
   - **Content type**: `application/json`
   - **Events**: "Pull requests" 선택
   - **Active** 체크


**애플리케이션 실행**
```bash
streamlit run main.py
```

## 📁 프로젝트 구조
```
pr-assistant/
├── main.py                          # 로그인 페이지
├── api/
│   └── github_api.py                # GitHub API 래퍼
├── azure_services/
│   ├── openai.py                    # Azure OpenAI 서비스
│   └── search.py                    # Azure Search 서비스
├── data/
│   ├── create-code-convention.py    # 코드 컨벤션 생성 스크립트
│   ├── python-code-convention.md    # Python 코드 컨벤션 문서
│   └── upload-code-convention.py    # 컨벤션 업로드 스크립트
├── pages/
│   ├── home.py                      # Repository 목록
│   ├── pr_detail.py                 # PR 상세 및 리뷰
│   └── repository_detail.py         # PR 목록
├── prompts/
│   └── code-review.txt              # 코드 리뷰 프롬프트 템플릿
├── service/
│   └── code_reviewer.py             # 코드 리뷰 서비스 로직
├── test/                            # 테스트 코드
└── utils/
    └── file_util.py                 # 파일 유틸리티
```

## TODO

### 완료
- [x] GitHub Token 로그인 기능
- [x] Repository 목록 조회
- [x] PR 목록 조회 (main 브랜치 기준)
- [x] PR 상세 정보 확인 (커밋, 파일 변경, 코멘트)
- [x] 커밋별 코멘트 작성
- [x] 파일별 코멘트 작성
- [x] PR 전체 코멘트 작성
- [x] PR 병합 기능 (merge/squash/rebase)
- [x] 내 리뷰 필요한 PR 필터링
- [x] Azure OpenAI 연동
- [x] Azure AI Search 구성
- [x] AI 리뷰 생성 기능
- [x] Azure Function 자동 리뷰
- [x] GitHub Webhook 연동
- [x] 설정 페이지 (자동 리뷰 ON/OFF)

### 예정
- [ ] 세션 만료 시간 설정
- [ ] 로딩 UI 개선



## ✨ 회고
GitHub 코드 리뷰는 개발 프로세스의 핵심이지만, Git/GitHub에 익숙하지 않은 관리자나 리뷰어에게는 진입 장벽이 꽤 높다. 단순히 UI만 제공하는 게 아니라, AI를 활용해서 리뷰 품질까지 높일 수 있다면 훨씬 더 가치 있는 도구가 될 거라는 생각으로 프로젝트를 시작했다.

처음엔 "AI한테 코드 주고 리뷰 요청하면 되겠지" 정도로 생각했는데, 막상 해보니 그렇게 간단하지 않았다. 토큰 제한에 걸리고, 컨텍스트가 부족해서 엉뚱한 리뷰가 나오고, 품질도 들쭉날쭉했다. 이 문제들을 해결하려고 Azure AI Search로 관련 문서를 먼저 찾아주고, 프롬프트를 구조화하고, 관리자가 최종 검토하는 프로세스를 넣음으로써, AI를 자동화 도구가 아니라 "리뷰 초안을 작성해주는 보조자"가 현실적인 것 같았다.

프로젝트를 진행하면서 느낀 건, AI한테 좋은 결과를 받으려면 모델 성능보다 **"어떤 정보를 어떻게 줄 것인가"**가 훨씬 중요하다는 거였다. 그리고 최신 기술이라고 무조건 쓰는 게 아니라, 상황에 맞는 적절한 도구를 고르는 게 핵심이었다. 예를 들어 코드 컨벤션을 찾을 때는 복잡한 AI 검색보다 단순하게 키워드 + 의미 기반 검색을 섞는 게 더 잘 맞았다.

자동화 기능을 만들면서 **"완전 자동화"**가 오히려 위험할 수 있다는 걸 깨달았다. 잘못된 리뷰가 자동으로 올라가면 혼란스러울 수 있으니까, 자동 리뷰를 켜고 끌 수 있게 하고 관리자가 최종 승인하는 구조로 만들었다. 편리함도 중요하지만, 사람이 반드시 확인해야 할 지점은 명확히 해두는 게 필요하다는 걸 배웠다.

이번에 MVP를 직접 만들어보면서 **"문제를 어떻게 해결할지 설계하는 능력"이 더 중요해지고 있다**는 걸 실감했다. 기술 자체보다 그걸 어떻게 조합하고 활용하느냐가 결과물의 품질을 좌우한다는 교훈을 얻었다.