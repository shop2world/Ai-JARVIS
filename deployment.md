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
1. Go to Web tab in PythonAnywhere dashboard
2. Click "Add a new web app"
3. Choose manual configuration
4. Select Python 3.8
5. Set virtual environment path: `/home/your_username/.virtualenvs/ai_jarvis`

### 5. Environment Variables
Add in Web tab's Environment variables section:

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

