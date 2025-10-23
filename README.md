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
- **Azure Blob Storage**: 컨벤션/가이드 문서 저장
- **Azure Function**: 자동 리뷰 트리거 및 처리

## 📖 사용 흐름

### 수동 리뷰 모드
1. **PR-Assistant 웹페이지 접속**
2. **GitHub 저장소 연동 및 PR 목록 확인**
3. **리뷰할 PR 선택**
4. **🤖 AI 리뷰 요청 버튼 클릭**
5. **AI가 코드 컨벤션 기반 리뷰 생성**
6. **관리자가 리뷰 내용 검토 및 수정**
7. **GitHub에 리뷰 등록** ✅

### 자동 리뷰 모드 (예정)
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

## 📁 프로젝트 구조
```
pr-assistant/
├── main.py                 # 로그인 페이지
├── pages/
│   ├── home.py            # Repository 목록
│   ├── repository_detail.py  # PR 목록
│   ├── pr_detail.py       # PR 상세 및 리뷰
│   └── settings.py        # AI 설정 (예정)
├── utils/
│   └── github_api.py      # GitHub API 래퍼
└── azure_functions/       # Azure Function 코드 (예정)
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

### 진행중 🔄
- [ ] Azure OpenAI 연동
- [ ] Azure AI Search 구성
- [ ] Blob Storage 문서 업로드
- [ ] AI 리뷰 생성 기능

### 예정
- [ ] 세션 만료 시간 설정
- [ ] 로딩 UI 개선
- [ ] Azure Function 자동 리뷰
- [ ] GitHub Webhook 연동
- [ ] 설정 페이지 (자동 리뷰 ON/OFF)