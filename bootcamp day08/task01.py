import requests
from bs4 import BeautifulSoup
from task00 import normalize_url, build_headers
import time

def get_html(url: str,*,timeout: float = 5.0,retries: int = 2,):
    normalized_url= normalize_url(url)
    headers= build_headers()
    last_exception= None
    
    for attempt in range(retries + 1):
        try: 
            response= requests.get(
            normalized_url,
            headers= headers,
            timeout= timeout
        )
            
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
            
        
        except (requests.RequestException, Exception) as e:
            last_exception = e
            if attempt < retries:
                time.sleep(0.5)
                continue
    raise last_exception
    
if __name__ == "__main__":
     soup = get_html("https://www.amazon.com/robots.txt")
     print(type(soup), '\n', soup) 