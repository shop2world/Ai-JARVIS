# Deployment Guide for AI-JARVIS

## PythonAnywhere Deployment Guide

### 1. Initial Setup
1. Create a PythonAnywhere account at [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Login to your account
3. Open a Bash console from the Dashboard

### 2. Virtual Environment Setup
```bash
# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.8 ai_jarvis

# Activate virtual environment
workon ai_jarvis

# Verify virtual environment
which python
# Should show: /home/your_username/.virtualenvs/ai_jarvis/bin/python
```

### 3. Project Setup
```bash
# Clone the repository
git clone https://github.com/shop2world/Ai-JARVIS.git
cd Ai-JARVIS

# Install requirements
pip install -r requirements.txt
```

### 4. Web App Configuration

1. **Basic Web App Setup**
   - Click 'Web' tab in PythonAnywhere dashboard
   - Click 'Add a new web app' button
   - Confirm domain name (e.g., your_username.pythonanywhere.com)
   - Select 'Manual configuration'
   - Choose Python 3.8

2. **Code Configuration**
   - Source code: `/home/your_username/Ai-JARVIS`
   - Working directory: `/home/your_username/Ai-JARVIS`
   - WSGI configuration file: `/var/www/your_username_pythonanywhere_com_wsgi.py`

3. **Virtual Environment Setup**
   - In Virtualenv section, enter path:
   `/home/your_username/.virtualenvs/ai_jarvis`

4. **Static Files Setup**
   - In Static files section:
     - URL: `/static/`
     - Directory: `/home/your_username/Ai-JARVIS/staticfiles`

### 5. Environment Variables

1. **Setting Environment Variables**
   - Scroll down in Web tab
   - Find 'Environment variables' section
   - Click 'Add a new variable'

2. **Required Environment Variables**
```bash
OPENAI_API_KEY=your_openai_api_key
SCRAPINGBEE_API_KEY=your_scrapingbee_api_key
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=False
ALLOWED_HOSTS=your_username.pythonanywhere.com
```

### 6. WSGI Configuration

1. **Edit WSGI File**
```python
import os
import sys

# Project path
path = '/home/your_username/Ai-JARVIS'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ai_web_scraper.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 7. Database and Static Files
```bash
# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate
```

### 8. Final Steps
1. Reload the web app from the Web tab
2. Visit your site at: `https://your_username.pythonanywhere.com`

## Troubleshooting

### Common Issues

1. **DisallowedHost Error**
   - Add to ALLOWED_HOSTS in settings.py:
   ```python
   ALLOWED_HOSTS = [
       'your_username.pythonanywhere.com',
       'localhost',
       '127.0.0.1',
   ]
   ```

2. **Static Files Not Loading**
   - Verify static files path
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT setting

3. **API Connection Issues**
   - Verify API keys in environment variables
   - Check API quotas

4. **500 Server Error**
   - Check error logs
   - Verify DEBUG setting
   - Check file permissions

### Logs
- Access logs from Web tab
- Error log: `/var/log/your_username.pythonanywhere.com.error.log`
- Server log: `/var/log/your_username.pythonanywhere.com.server.log`

## Support
- Contact: Frank Kim
- Email: info@shop2world.com
- Twitter: [@salecoupon](https://x.com/salecoupon)
