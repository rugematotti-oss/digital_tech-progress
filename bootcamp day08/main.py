import json
from task09 import scrape_books
root = "https://books.toscrape.com/catalogue/category/books/"
data = json.loads(scrape_books(root + "food-and-drink_33/index.html"))
print(type(data), len(data), data[0].keys())