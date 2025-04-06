# GitHub MCP Server 테스트 저장소

이 저장소는 GitHub MCP(Mixed Computational Platform) 서버의 기능을 시험해보기 위한 테스트 저장소입니다. GitHub API와 LLM을 활용하여 다양한 소스 관리 및 워크플로우 기능을 테스트하고 활용하는 방법을 보여줍니다.

## 시험 가능한 기능 목록

1. **저장소 관리 핵심 기능**
   - 저장소 목록 조회
   - 특정 저장소 내용 확인
   - 최근 커밋 확인
   - 파일 생성 및 삭제
   - 브랜치 관리

2. **파일 관리**
   - 파일 생성 및 수정
   - 파일 내용 조회/분석
   - 파일 삭제
   - 코드 분석 및 개선

3. **브랜치 관리**
   - 브랜치 생성
   - 브랜치 간 병합
   - 브랜치 전략

4. **이슈 및 PR(Pull Request) 관리**
   - 이슈 생성 및 관리
   - PR 생성 및 병합
   - 코드 리뷰 커멘트 작성

5. **워크플로우 자동화**
   - GitHub Actions 구성
   - 워크플로우 스크립트 작성
   - 배포 파이프라인 설정

## LLM과의 연동 예시

LLM을 활용하여 GitHub MCP 기능을 활용하는 방법의 예시입니다. 아래는 각 기능별 테스트 예시입니다:

### 1. 저장소 관리 핵심 기능 예시

#### 저장소 목록 조회
```
내 GitHub 계정의 저장소 목록을 보여주고, 각 저장소의 주요 정보(언어, 별 수, 최근 업데이트 날짜)를 요약해줘.
```

#### 특정 저장소 내용 확인
```
iworkist/test_github_mcp 저장소의 파일 구조를 보여주고, 핵심 파일들의 내용과 목적을 간략히 설명해줘.
```

#### 최근 커밋 확인
```
iworkist/test_github_mcp 저장소의 최근 5개 커밋 내역을 보여주고, 각 커밋에서 어떤 변경사항이 있었는지 요약해줘.
```

#### 파일 생성 및 삭제
```
temp.txt 파일을 만들어줘. 테스트용이야.
iworkist/test_github_mcp 저장소에서 불필요한 temp.txt 파일을 삭제해줘. 커밋 메시지는 "Remove temporary test file"로 설정해줘.
```

### 2. 파일 관리 예시

#### 파일 생성 및 수정
```
Python으로 작성된 웹 스크래퍼를 만들어서 내 test_github_mcp 저장소에 webscraper.py 파일로 추가해줘. BeautifulSoup과 requests 라이브러리를 사용하는 코드로 작성해줘.
```

#### 파일 내용 분석 및 개선
```
iworkist/test_github_mcp 저장소의 helloworld.py 파일에 새로운 함수 goodbye()를 추가해줘. 이 함수는 "Goodbye, GitHub MCP World!"를 반환하도록 해줘.
```

현재 helloworld.py 파일에는 hello() 함수와 새로 추가된 goodbye() 함수가 있으며, main() 함수에서는 두 함수의 결과를 모두 출력합니다:
```python
def hello():
    """Simple function that returns a greeting message"""
    return "Hello, GitHub MCP World!"

def goodbye():
    """Simple function that returns a farewell message"""
    return "Goodbye, GitHub MCP World!"

def main():
    """Main function to print the greeting"""
    message = hello()
    print(message)
    
    # Also print the goodbye message
    farewell = goodbye()
    print(farewell)
```

### 3. 브랜치 관리 예시

#### 브랜치 생성
```
iworkist/test_github_mcp 저장소에 'update-readme' 브랜치를 새로 만들어줘. 이 브랜치는 main 브랜치를 기준으로 생성해줘.
```

#### 브랜치 간 병합
```
iworkist/test_github_mcp 저장소의 'update-readme' 브랜치를 main 브랜치로 병합해줘. 병합 시 충돌이 있으면 자동으로 해결하고, 병합 커밋 메시지는 "Merge updated README into main"으로 설정해줘.
```

#### 브랜치 전략 및 보호 브랜치 설정
```
iworkist/test_github_mcp 저장소에서 'development' 브랜치로 분기한 다음, config.json 파일을 수정해서 debug 모드를 true로 변경해줘. 변경 후 해당 내용을 커밋하고 'development' 브랜치에 푸시해줘.
```

### 4. 이슈 및 PR 관리 예시

#### 이슈 생성 및 관리
```
test_github_mcp 저장소에 "API 기능 확장 필요" 제목으로 새 이슈를 생성해줘. 이슈 내용에는 현재 API 호환성과 확장이 필요한 부분을 3가지 항목으로 정리해줘.
```

#### 이슈에 코멘트 추가
```
iworkist/test_github_mcp 저장소의 이슈 #3에 코멘트를 추가해줘. 이슈의 진행상태에 대한 업데이트 내용을 작성하고, 앞으로 언제 PR을 보낼 수 있는지 언급해줘.
```

#### PR 생성
```
iworkist/test_github_mcp 저장소에 새 PR을 만들어줘. 'update-readme' 브랜치의 변경사항을 main 브랜치로 병합하는 PR이며. PR 제목은 "Update README.md to match current functionality"로 하고, 설명에는 변경사항 요약과 테스트 방법을 포함해줘.
```

#### PR 검토 및 코멘트
```
iworkist/test_github_mcp 저장소의 PR #3을 검토하고, 코드 품질에 대한 검토 코멘트를 작성해줘. 특히 에러 처리, 변수명 선택, 알고리즘 성능 최적화 등 측면에서 개선점을 지적해줘.
```

### 5. 워크플로우 자동화 예시

#### GitHub Actions 워크플로우 작성
```
iworkist/test_github_mcp 저장소에 GitHub Actions 워크플로우 파일을 추가해줘. Python 코드에 대한 기본적인 테스트와 코드 품질을 확인하는 CI 워크플로우를 만들어줘. main 브랜치와 PR에서 트리거되도록 설정해줘.
```

#### 워크플로우 스크립트 작성
```
iworkist/test_github_mcp 저장소에 있는 webscraper.py 파일에 대한 워크플로우 테스트 스크립트를 test_webscraper.py 파일로 만들어줘. 특히 이 테스트가 매일 자동으로 실행되도록 GitHub Actions 스케줄 워크플로우도 만들어줘.
```

#### 배포 파이프라인 설정
```
iworkist/test_github_mcp 저장소에 배포 워크플로우 스크립트를 만들어줘. main 브랜치에 새 태그가 생성될 때 자동으로 Python 패키지를 빌드하고 GitHub Releases에 업로드하는 워크플로우를 작성해줘.
```

### 6. 고급 활용 예시

#### 완전한 기능의 예제
```
iworkist/test_github_mcp 저장소에서 다음 작업을 순차적으로 수행해줘:
1. 'feature/data-analysis' 브랜치를 새로 만들기
2. 간단한 데이터 분석을 위한 Python 스크립트(data_analyzer.py)를 생성
3. 해당 스크립트에 대한 테스트 파일도 추가
4. 이 변경사항을 PR로 생성하여 main 브랜치로 병합 요청하기
```

#### 저장소 분석 및 개선 제안
```
test_github_mcp 저장소의 코드를 분석하고, 코드 구조, 주요 기능, 개선 가능한 부분에 대한 보고서를 작성해줘. 특히 Python 코딩 관행을 준수하고 있는지 확인하고, 개선 방안을 이슈로 등록해줘.
```

## 사용 방법

1. LLM과 대화할 때 위 예시 프롬프트를 사용하여 GitHub 관련 작업을 수행할 수 있습니다.
2. LLM은 GitHub API를 통해 요청된 작업을 수행하고 결과를 보고합니다.
3. 복잡한 작업의 경우, 단계별로 나눠서 수행하면 더 효과적입니다.

## 예시 커밋 및 변경 내역

지난 커밋 내역:
```
최근 커밋 내역 (2025-04-06):
1. "Add goodbye() function to helloworld.py"
   - hello() 함수와 함께 goodbye() 함수 추가
   - main() 함수가 두 메시지를 모두 출력하도록 수정

2. "Remove temporary test file"
   - temp.txt 파일 삭제 시도 (현재 API 제한으로 인해 직접 삭제는 불가능)

3. "Add temp.txt for testing"
   - 테스트용 임시 파일 생성

4. "README에 모든 시험 가능 기능에 대한 예제 추가"
   - README.md 파일에 포괄적인 사용 예제 추가
   - 브랜치, PR, 자동화 워크플로우 관련 설명 추가
```

## 주의사항

- 권한이 없는 저장소나 보호된 브랜치는 이 방식으로 변경하지 못할 수 있습니다.
- 대규모 프로젝트의 경우, 복잡한 코드베이스를 LLM이 이해하는 데 한계가 있을 수 있습니다.
- 민감한 변경사항은 직접 검토 수준으로 검토한 후 적용하는 것이 안전합니다.
- 워크플로우 자동화 시 GitHub 계정의 할당량 사용량을 확인하세요.
