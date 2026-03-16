from task01 import get_html

def count_paragraph_links(url: str) -> int:

    soup = get_html(url)
    paragraphs = soup.find_all('p')
    total_links = 0
    for p in paragraphs:
        links = p.find_all('a', href=True)
        total_links += len(links)
    
    return total_links