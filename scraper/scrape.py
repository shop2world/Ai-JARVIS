import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

def scrape_website(website):
    try:
        api_key = os.getenv('SCRAPINGBEE_API_KEY')
        endpoint = 'https://app.scrapingbee.com/api/v1/'
        
        params = {
            'api_key': api_key,
            'url': website,
            'render_js': 'true'
        }
        
        response = requests.get(endpoint, params=params)
        return response.text
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
        raise

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ] 