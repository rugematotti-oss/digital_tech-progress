from task01 import get_html

def list_all_links(url: str) -> list[str]:
    soup= get_html(url)
    links= []
    for a_tag in soup.find_all('a', href=True):
     links.append(a_tag['href'])

    return links
