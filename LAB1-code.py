import requests
from bs4 import BeautifulSoup
import pandas as pd

product_data = []
for page_num in range(1, 2):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products_section = soup.find('ol')
    product_items = products_section.find_all('article', class_='product_pod')
    
    for item in product_items:
        img_tag = item.find('img')
        product_name = img_tag.attrs['alt']
        rating_tag = item.find('p')
        product_rating = rating_tag['class'][1]
        product_price_range = item.find('p', class_='price_color').text
        product_price_range = float(product_price_range[1:])
        stock_status_availability = item.find('p', class_='instock availability').text.strip()
        
        product_data.append([product_name, product_price_range, product_rating, stock_status_availability])


df_products = pd.DataFrame(product_data, columns=['Product_Name', 'Price', 'Rating', 'Availability'])
df_products.to_csv('lab1_Dataset-of-the-books.csv', index=False)
