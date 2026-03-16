from task01 import get_html
import json
from urllib.parse import urljoin


def scrape_books(category_url: str) -> str:
    books = []
    current_url = category_url
    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    
    while current_url:
        soup = get_html(current_url)

        book_cards = soup.find_all('article', class_='product_pod')
        
        for card in book_cards:

            h3 = card.find('h3')
            if h3:
                title_link = h3.find('a')
                title = title_link.get('title', '') if title_link else ''
            else:
                title = ''
            price_elem = card.find('p', class_='price_color')
            if price_elem:
                price_text = price_elem.get_text().strip()
                price = float(price_text.replace('£', '').replace('Â', '').strip())
            else:
                price = 0.0
            
            availability_elem = card.find('p', class_='availability')
            if availability_elem:
                availability_text = availability_elem.get_text().strip()
                availability = 'In stock' in availability_text
            else:
                availability = False
            star_rating = card.find('p', class_='star-rating')
            if star_rating:
                rating_classes = star_rating.get('class', [])
                rating_word = rating_classes[1] if len(rating_classes) > 1 else 'One'
                rating = rating_map.get(rating_word, 1)
            else:
                rating = 1
            
            books.append({
                "title": title,
                "rating": rating,
                "price": price,
                "availability": availability
            })
        
        next_li = soup.find('li', class_='next')
        if next_li:
            next_link = next_li.find('a')
            if next_link:
                next_href = next_link.get('href')
                current_url = urljoin(current_url, next_href)
            else:
                current_url = None
        else:
            current_url = None
    
  
    return json.dumps(books)

