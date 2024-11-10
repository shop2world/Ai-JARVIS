from django.shortcuts import render
from bs4 import BeautifulSoup
from django.contrib import messages
import os
from dotenv import load_dotenv
from openai import OpenAI
from .scrape import scrape_website

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_ai_analysis(content, description):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes web content."},
                {"role": "user", "content": f"Please analyze this content based on the following request: {description}\n\nContent: {content}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI 분석 중 오류 발생: {str(e)}"

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url', '').strip()
        description = request.POST.get('description', '').strip()
        
        if not url:
            messages.error(request, 'URL을 입력해주세요.')
            return render(request, 'scraper/index.html')
            
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            # ScrapingBee를 통한 웹 스크래핑
            html_content = scrape_website(url)
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 웹 페이지 콘텐츠 추출
            main_content = soup.get_text()
            
            # AI 분석 수행
            ai_analysis = get_ai_analysis(main_content[:4000], description)
            
            parsed_result = {
                'title': soup.title.string if soup.title else 'No title found',
                'description': description,
                'url': url,
                'ai_analysis': ai_analysis
            }
            
            return render(request, 'scraper/result.html', {
                'parsed_result': parsed_result,
                'dom_content': str(soup.prettify())
            })
            
        except Exception as e:
            messages.error(request, f'스크래핑 중 오류가 발생했습니다: {str(e)}')
            
    return render(request, 'scraper/index.html') 