# GitHub MCP Server 테스트 저장소

이 저장소는 GitHub MCP(Mixed Computational Platform) 서버의 기능을 시험해보기 위한 테스트 저장소입니다. GitHub API와 LLM을 연결하여 다양한 코드 관리 및 자동화 기능을 테스트하고 활용하는 방법을 보여줍니다.

## 시험 가능한 기능 목록

1. **저장소 정보 조회**
   - 저장소 목록 확인
   - 특정 저장소 내용 탐색
   - 커밋 내역 조회

2. **파일 관리**
   - 파일 생성 및 업로드
   - 파일 내용 업데이트
   - 파일 삭제

3. **브랜치 관리**
   - 브랜치 생성
   - 브랜치 간 머지
   - 브랜치 전환

4. **이슈 및 PR(Pull Request) 관리**
   - 이슈 생성 및 관리
   - PR 생성 및 리뷰
   - 코드 리뷰 코멘트 작성

5. **자동화 스크립트**
   - GitHub Actions 구성
   - 자동 테스트 실행
   - 자동 배포 파이프라인

## LLM과의 연동 예제

LLM을 활용하여 GitHub MCP 기능을 활용하는 방법의 예제입니다. 아래는 각 기능별 프롬프트 예시입니다:

### 1. 저장소 정보 조회 예제

#### 저장소 목록 확인
```
내 GitHub 계정의 저장소 목록을 보여주고, 각 저장소의 주요 정보(언어, 별 수, 최근 업데이트 날짜)를 요약해줘.
```

#### 특정 저장소 내용 탐색
```
iworkist/test_github_mcp 저장소의 파일 구조를 보여주고, 핵심 파일들의 내용과 목적을 간략히 설명해줘.
```

#### 커밋 내역 조회
```
iworkist/test_github_mcp 저장소의 최근 5개 커밋 내역을 보여주고, 각 커밋에서 어떤 변경사항이 있었는지 요약해줘.
```

### 2. 파일 관리 예제

#### 파일 생성 및 업로드
```
Python으로 간단한 웹 스크래퍼를 만들어서 내 test_github_mcp 저장소에 webscraper.py 파일로 추가해줘. BeautifulSoup와 requests 라이브러리를 사용하는 코드로 작성해줘.
```

#### 파일 내용 업데이트
```
iworkist/test_github_mcp 저장소의 helloworld.py 파일에 새로운 함수 goodbye()를 추가해줘. 이 함수는 "Goodbye, GitHub MCP World!"를 반환하도록 해줘.
```

#### 파일 삭제
```
iworkist/test_github_mcp 저장소에서 불필요한 temp.txt 파일을 삭제해줘. 커밋 메시지는 "Remove temporary test file"로 설정해줘.
```

### 3. 브랜치 관리 예제

#### 브랜치 생성
```
iworkist/test_github_mcp 저장소에 'feature/user-authentication' 브랜치를 새로 만들어줘. 이 브랜치는 main 브랜치를 기반으로 생성해줘.
```

#### 브랜치 간 머지
```
iworkist/test_github_mcp 저장소의 'feature/new-ui' 브랜치를 main 브랜치로 머지해줘. 머지 시 충돌이 있으면 보수적으로 해결하고, 머지 커밋 메시지는 "Merge new UI features into main"으로 설정해줘.
```

#### 브랜치 전환 및 복수 브랜치 작업
```
iworkist/test_github_mcp 저장소에서 'development' 브랜치로 전환한 다음, config.json 파일을 수정해서 debug 모드를 true로 변경해줘. 변경 후 해당 내용을 커밋하고 'development' 브랜치에 푸시해줘.
```

### 4. 이슈 및 PR 관리 예제

#### 이슈 생성 및 관리
```
test_github_mcp 저장소에 "API 기능 개선 필요" 제목으로 새 이슈를 생성해줘. 이슈 내용에는 현재 API 한계점과 개선이 필요한 부분을 3가지 항목으로 정리해줘.
```

#### 이슈에 코멘트 추가
```
iworkist/test_github_mcp 저장소의 이슈 #2에 코멘트를 추가해줘. 이슈의 문제점에 대한 해결 방안을 제시하고, 내가 직접 PR을 만들 수 있다고 제안해줘.
```

#### PR 생성
```
iworkist/test_github_mcp 저장소에 새 PR을 만들어줘. 'feature/error-handling' 브랜치의 변경사항을 main 브랜치로 반영하는 PR이야. PR 제목은 "Improve error handling for API requests"로 하고, 설명에는 변경사항 요약과 테스트 방법을 포함해줘.
```

#### PR 리뷰 및 코멘트
```
iworkist/test_github_mcp 저장소의 PR #3을 검토하고, 코드 품질 개선을 위한 리뷰 코멘트를 작성해줘. 특히 에러 처리 방식, 변수명 작명 규칙, 그리고 성능 최적화 측면에서 피드백을 제공해줘.
```

### 5. 자동화 스크립트 예제

#### GitHub Actions 워크플로우 생성
```
iworkist/test_github_mcp 저장소에 GitHub Actions 워크플로우 파일을 추가해줘. Python 코드에 대한 기본적인 린트와 유닛 테스트를 실행하는 CI 워크플로우를 만들어줘. main 브랜치와 PR에서 트리거되도록 설정해줘.
```

#### 자동 테스트 실행 구성
```
iworkist/test_github_mcp 저장소에 있는 webscraper.py 파일에 대한 자동 테스트 스크립트를 test_webscraper.py 파일로 만들어줘. 그리고 이 테스트가 매일 자정에 자동 실행되도록 GitHub Actions 스케줄 워크플로우도 만들어줘.
```

#### 자동 배포 파이프라인 구성
```
iworkist/test_github_mcp 저장소에 배포 자동화 워크플로우를 만들어줘. main 브랜치에 새 태그가 생성될 때 자동으로 Python 패키지를 빌드하고 GitHub Releases에 업로드하는 워크플로우를 구성해줘.
```

### 6. 고급 활용 예제

#### 여러 기능의 조합
```
iworkist/test_github_mcp 저장소에서 다음 작업을 순차적으로 수행해줘:
1. 'feature/data-analysis' 브랜치를 새로 만들기
2. 간단한 데이터 분석을 위한 Python 스크립트(data_analyzer.py)를 생성
3. 해당 스크립트에 대한 단위 테스트 파일도 추가
4. 이 변경사항을 PR로 생성하여 main 브랜치로 머지 요청하기
```

#### 저장소 분석 및 개선 제안
```
test_github_mcp 저장소의 코드를 분석하고, 코드 구조, 주요 기능, 개선 가능한 부분에 대한 보고서를 작성해줘. 특히 Python 코딩 표준을 따르고 있는지 평가하고, 개선 방안을 이슈로 등록해줘.
```

## 사용 방법

1. LLM과 대화할 때 위 예제 프롬프트를 참고하여 GitHub 관련 작업을 요청합니다.
2. LLM은 GitHub API를 통해 요청된 작업을 수행하고 결과를 보고합니다.
3. 복잡한 작업의 경우, 단계별로 나누어 요청하면 더 효과적입니다.

## 예상 결과 예시

### 저장소 목록 확인 결과
```
iworkist 계정의 GitHub 저장소 목록:
1. bitcoinpy - Python으로 비트코인 프로그래밍 관련 저장소 (★23)
   - 언어: Python
   - 생성일: 2020-03-11
2. test_github_mcp - GitHub MCP 서버 테스트 저장소
   - 언어: Python
   - 생성일: 2025-04-06
...
```

### PR 생성 결과
```
PR이 성공적으로 생성되었습니다!

제목: Improve error handling for API requests
URL: https://github.com/iworkist/test_github_mcp/pull/4
상태: Open
브랜치: feature/error-handling → main

PR 설명에는 다음 내용이 포함되어 있습니다:
- API 요청 시 오류 처리 개선
- 타임아웃 및 재시도 메커니즘 추가
- 상세한 오류 로깅 구현
...
```

## 주의사항

- 민감한 정보나 보안 관련 코드는 이 방식으로 관리하지 않는 것이 좋습니다.
- 대규모 프로젝트의 경우, 전체 코드베이스를 LLM이 이해하는 데 한계가 있을 수 있습니다.
- 중요한 변경사항은 항상 수동으로 검토한 후 적용하는 것이 안전합니다.
- 자동화 스크립트 실행 시 GitHub 계정의 액션 사용량 제한을 확인하세요.
