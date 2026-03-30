# 윈도우 실행파일(EXE) 제작 가이드

이 프로젝트(`gui_main.py`)를 윈도우에서 단독 실행 가능한 `.exe` 파일로 만드는 방법입니다.

## 1. 사전 준비
파이썬이 설치된 환경의 터미널(PowerShell 또는 CMD)에서 다음 라이브러리를 설치합니다.
```powershell
pip install pyinstaller
```

## 2. 빌드 명령어
프로젝트 루트 폴더(`d:\python\photokey`)에서 아래 명령어를 실행합니다.
```powershell
pyinstaller --noconsole --onefile --add-data "fab2;fab2" --add-data "static;static" gui_main.py
```

### 옵션 상세 설명
*   `--noconsole`: 프로그램 실행 시 검은색 터미널(콘솔) 창이 뜨지 않게 합니다.
*   `--onefile`: 모든 라이브러리와 리소스를 하나의 `.exe` 파일로 합칩니다.
*   `--add-data "fab2;fab2"`: 로직이 담긴 `fab2` 폴더를 포함합니다.
*   `--add-data "static;static"`: 로고 이미지 등이 담긴 `static` 폴더를 포함합니다.
*   `gui_main.py`: 빌드 대상인 메인 스크립트 파일입니다.

## 3. 결과 확인 및 배포
1.  명령어 실행 후 새롭게 생성된 **`dist`** 폴더로 이동합니다.
2.  폴더 안의 `gui_main.exe` 파일을 실행하여 정상 동작을 확인합니다.
3.  다른 사용자에게 전달할 때는 `dist\gui_main.exe` 파일 하나만 전달하면 됩니다.

## 4. 참고 사항
현재 코드에는 빌드된 EXE 환경에서도 경로를 올바르게 찾을 수 있도록 아래와 같은 처리가 되어 있습니다.
*   `sys.frozen` 체크를 통해 실행 환경(EXE vs 스크립트)을 자동 감지합니다.
*   EXE 실행 시 `sys._MEIPASS`(임시 폴더)로 작업 디렉토리를 자동 변경합니다.
*   결과 파일은 항상 프로그램을 **처음 실행했던 위치**에 생성됩니다.
