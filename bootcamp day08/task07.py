from task01 import get_html
from task02 import scrape_title
import random


def tarzan(url: str,n: int,*,seed: int | None = None) -> list[str]:
    if seed is not None:
        random.seed(seed)
    titles = []
    current_url = url

    for _ in range(n):
        title = scrape_title(current_url)
        titles.append(title)
        soup = get_html(current_url)
        content = soup.find('div', {'id': 'mw-content-text'})
        if not content:
            content = soup.find('div', {'class': 'mw-parser-output'})
        if not content:
            content = soup
        all_links = content.find_all('a', href=True)
        valid_links = []
        for link in all_links:
            href = link['href']
            if href.startswith('/wiki/'):
                if ':' not in href:
                    valid_links.append(href)
        if not valid_links:
            break
        next_path = random.choice(valid_links)
        current_url = f"https://en.wikipedia.org{next_path}"
    
    return titles
