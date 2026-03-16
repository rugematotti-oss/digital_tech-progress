from task01 import get_html
def scrape_paragraph(url: str) -> str:
 soup= get_html(url)

 paragraphs= soup.find_all('p')

 for p in paragraphs:
  text= p.get_text().strip()
  if text:
      return str(p)
  return""