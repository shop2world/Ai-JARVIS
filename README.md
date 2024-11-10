# AI Web Scraper

A Django-based web scraper that uses ScrapingBee API and OpenAI API to analyze web content.
Features
Web content scraping using ScrapingBee API
Content analysis using OpenAI GPT
Clean and simple user interface
Prerequisites
Python 3.8+
ScrapingBee API key
OpenAI API key
Local Installation
Clone the repository:
Bash
Create and activate virtual environment:
Bash
Install required packages:
Bash
Set up environment variables:
Bash
Run migrations:
Bash
Start development server:
Bash
PythonAnywhere Deployment Guide
Create and login to PythonAnywhere account
Create virtual environment in Bash console:
Bash
Clone the project:
Bash
Install required packages:
Bash
Configure PythonAnywhere web app:
Create new web app from Web tab
Select Django framework
Choose Python 3.8
Set virtual environment path: /home/your_username/.virtualenvs/ai_scraper
Modify WSGI configuration file:
Set environment variables:
Add in Web tab's Environment variables section:
Configure static files:
Bash
Run migrations:
Bash
Reload web app
API Key Setup
ScrapingBee
Sign up at ScrapingBee
Get API key
Set in .env file or environment variables
OpenAI
Sign up at OpenAI
Get API key
Set in .env file or environment variables
Usage
Access the web application
Enter URL to analyze
Enter analysis description
Click "Scrape and Parse" button
View analysis results
Security Notes
Never commit your .env file
Keep your API keys secure
Set DEBUG=False in production
License
MIT License
Contributing
1. Fork the repository
Create your feature branch
Commit your changes
4. Push to the branch
Create a Pull Request
Support
Please open an issue for support.
Acknowledgments
OpenAI for providing GPT API
ScrapingBee for web scraping capabilities
Django framework
