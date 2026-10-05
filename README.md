# Python Git Auto Backup
# Python Git Auto Backup

파이썬 파일의 변경을 감지하고 GitHub에 자동으로 백업하는 리눅스용 프로그램입니다.

반복적으로 실행하던 `git add`, `git commit`, `git push` 작업을 파이썬으로 자동화하기 위해 만들었습니다.

## 주요 기능

- 2초 간격으로 파이썬 파일의 변경 확인
- 마지막 변경 감지 후 30초 동안 추가 변경이 없으면 자동 커밋
- 파일의 추가, 수정, 삭제 반영
- 커밋을 GitHub의 `main` 브랜치로 자동 푸시
- 푸시 실패 시 30초 간격으로 재시도
- 터미널에 변경 감지, 커밋, 업로드 결과 출력

## 개발 환경

- Ubuntu 18.04
- Python 3.6.9
- Git 2.17.1
- GitHub SSH 인증

파이썬 표준 라이브러리만 사용하므로 별도의 패키지 설치가 필요하지 않습니다.

## 실행 방법

Git 저장소의 `origin`과 SSH 인증을 먼저 설정해야 합니다. 자동 커밋에 사용할 Git 작성자 이름과 이메일도 설정되어 있어야 합니다.

프로젝트 폴더에서 다음 명령을 실행합니다.

```bash
python3 auto_backup.py
```

프로그램이 실행된 상태에서 같은 폴더 또는 하위 폴더의 `.py` 파일을 수정하고 저장하면 자동 백업됩니다.

종료하려면 `Ctrl+C`를 누릅니다.

## 동작 과정

1. Git에서 파이썬 파일 목록과 변경 상태를 가져옵니다.
2. 파일 이름, 내용, Git 상태를 SHA-256 해시로 계산합니다.
3. 이전 해시와 비교해 변경 여부를 확인합니다.
4. 마지막 변경 후 30초가 지나면 변경 내용을 커밋합니다.
5. `git push origin main`으로 GitHub에 업로드합니다.

## 실행 예시

```text
Auto backup start: /home/user/work/python/git-auto-backup
Python files will be uploaded 30 seconds after the last change.
Press Ctrl+C to exit.
[Detected] Changed. Wait for 30 seconds.
[Commit] Auto backup: 2026-10-01 10:18:04
[Complete] GitHub upload success
```

## 설정

`auto_backup.py`에서 확인 간격과 대기 시간을 변경할 수 있습니다.

```python
CHECK_INTERVAL = 2
WAIT_SECONDS = 30
```

시간 단위는 초입니다. 백업 대상 폴더는 `auto_backup.py`가 위치한 폴더입니다.

## 사용 시 참고 사항

- 자동 커밋 대상은 `.py` 파일입니다. README 등의 다른 파일은 수동으로 커밋해야 합니다.
- 프로그램이 실행 중일 때만 변경을 감시합니다.
- 코드 실행이나 문법 검사는 수행하지 않으므로 오류가 있는 코드도 백업될 수 있습니다.
- 인증 오류나 원격 저장소와의 충돌은 직접 해결해야 합니다.
- `.gitignore`로 새 파일의 추적을 제외할 수 있지만, 이미 추적 중인 파일에는 그대로 적용되지 않습니다.
- 업로드할 코드에 비밀번호나 API 키를 직접 작성하지 않아야 합니다.

## 학습한 내용

- Git의 스테이징, 커밋, 푸시 과정
- SSH 키를 이용한 GitHub 인증
- `subprocess`를 통한 외부 명령 실행
- 해시를 활용한 파일 변경 감지
- 시간 측정, 반복 처리, 예외 처리
