# Deployment Guide for AI-JARVIS

## PythonAnywhere Deployment Guide

### 1. Initial Setup
1. Create a PythonAnywhere account at [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Login to your account
3. Open a Bash console from the Dashboard

### 2. Virtual Environment Setup

# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.8 ai_jarvis

# Activate virtual environment
workon ai_jarvis


# Create virtual environment

### 3. Project Setup


# Clone the repository

### 4. Web App Configuration

1. **Web App 기본 설정**
   - PythonAnywhere 대시보드에서 'Web' 탭 클릭
   - 'Add a new web app' 버튼 클릭
   - 도메인 이름 확인 (예: your_username.pythonanywhere.com)
   - 'Manual configuration' 선택
   - Python 버전 3.8 선택

2. **Code 설정**
   - Source code: `/home/your_username/Ai-JARVIS`
   - Working directory: `/home/your_username/Ai-JARVIS`
   - WSGI configuration file: `/var/www/your_username_pythonanywhere_com_wsgi.py`

3. **Virtual Environment 설정**
   - Virtualenv 섹션에서 경로 입력:
   `/home/your_username/.virtualenvs/ai_jarvis`

4. **Static Files 설정**
   - Static files 섹션에서:
     - URL: `/static/`
     - Directory: `/home/your_username/Ai-JARVIS/staticfiles`

5. **WSGI 파일 설정**
   - WSGI configuration file 클릭하여 편집
   ```python
   import os
   import sys

   # 프로젝트 경로
   path = '/home/your_username/Ai-JARVIS'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'ai_web_scraper.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

6. **설정 확인 및 적용**
   - 모든 경로가 정확한지 확인
   - 'Reload' 버튼 클릭하여 변경사항 적용

**주의사항**:
- 모든 경로에서 'your_username'을 실제 PythonAnywhere 사용자명으로 변경
- 경로는 대소문자를 구분하므로 정확히 입력
- 프로젝트 디렉토리 구조가 올바른지 확인

### 5. Environment Variables

1. **Web App Configuration Page에서 환경 변수 설정**
   - PythonAnywhere 대시보드에서 'Web' 탭 클릭
   - 해당 웹 앱 섹션으로 스크롤
   - 'Environment variables' 섹션 찾기 (WSGI configuration file 섹션 아래에 있음)
   - 'Add a new variable' 버튼 클릭

2. **필요한 환경 변수 추가**

### 6. Static Files and Database

### 7. WSGI Configuration
Edit the WSGI configuration file:

### 8. Final Steps
1. Reload the web app from the Web tab
2. Visit your site at: `https://your_username.pythonanywhere.com`

## Troubleshooting

### Common Issues
1. **Static Files Not Loading**
   - Check static files configuration
   - Run collectstatic again

2. **API Connection Issues**
   - Verify API keys in environment variables
   - Check API quotas and limits

3. **500 Server Error**
   - Check error logs in Web tab
   - Verify DEBUG setting
   - Check file permissions

### Logs
- Access logs from the Web tab
- Error log: `/var/log/your_username.pythonanywhere.com.error.log`
- Server log: `/var/log/your_username.pythonanywhere.com.server.log`

