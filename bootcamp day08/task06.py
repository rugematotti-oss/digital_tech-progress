from task01 import get_html
from task00 import build_headers
import requests
import os
from urllib.parse import urljoin


def download_images(
    url: str,
    *,
    output_dir: str = "images",
) -> int:
    
    os.makedirs(output_dir, exist_ok=True)

    soup = get_html(url)

    content = soup.find('div', {'id': 'mw-content-text'})
    if not content:
        content = soup.find('div', {'class': 'mw-parser-output'})
    if not content:
        content = soup
    images = content.find_all('img')

    headers = build_headers() 
    
    count = 0
    
    for img in images:

        img_url = img.get('src')
        if not img_url:
            continue
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif img_url.startswith('/'):
            img_url = urljoin(url, img_url)
        
        width = img.get('width')
        height = img.get('height')
        if width and height:
            try:
                if int(width) < 50 or int(height) < 50:
                    continue
            except ValueError:
                pass
        filename = os.path.basename(img_url.split('?')[0])
        if not filename:
            filename = f"image_{count}.jpg"
        
        filepath = os.path.join(output_dir, filename)
        
        try:
            img_response = requests.get(img_url, headers=headers, timeout=10)
            img_response.raise_for_status()
            with open(filepath, 'wb') as f:
                f.write(img_response.content)
            
            count += 1
            print(f"Downloaded: {filename}")
            
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
            continue
    
    return count