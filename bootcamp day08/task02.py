import requests
from bs4 import BeautifulSoup
from task01 import get_html
import time

def scrape_title(url: str) -> str: 
    soup= get_html(url)
    if soup.title:
        return soup.title.string.strip()
    else:
        return ""
    
