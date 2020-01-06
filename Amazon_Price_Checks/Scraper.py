from bs4 import BeautifulSoup
import requests
import csv
from datetime import date
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

class Product:
    """
    Class that allows to track a products title & price from amazon.
    """
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def scrape_information(self):
            page = requests.get(self.url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.select('#productTitle')[0].get_text().strip()
            self.title = str(title).replace(',', '')
            price = soup.select("#priceblock_ourprice")[0].get_text().strip()
            self.number_price = float(price[0:-2].replace(',', '.'))


def save_product(product_class):
    with open(csv_name, 'a', encoding='utf-8') as f:
        csv_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([product_class.title, product_class.number_price, date])

csv_name = 'amazon_products.csv'
urls = ['https://www.amazon.de/You2Toys-07702210000-Eier-Shampoo-350-ml/dp/B002A9MMPU']

date = str(date.today())
df = pd.read_csv(csv_name, delimiter=',')
last_date = df['Date'].iloc[-1]

if last_date != date:
    product_1 = Product(csv_name, urls[0])
    product_1.scrape_information()
    save_product(product_1)
