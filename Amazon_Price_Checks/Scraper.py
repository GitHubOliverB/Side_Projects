from bs4 import BeautifulSoup
import requests
import csv
from datetime import date
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

urls = ['https://www.amazon.de/You2Toys-07702210000-Eier-Shampoo-350-ml/dp/B002A9MMPU']

date = str(date.today())
df = pd.read_csv('eier_shampoo.csv', delimiter=',')
last_date = df.Date[-1]

if last_date != date:
    for url in urls:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.select('#productTitle')[0].get_text().strip()
        price = soup.select("#priceblock_ourprice")[0].get_text().strip()
        number_price = float(price[0:-2].replace(',', '.'))
        with open('eier_shampoo.csv', 'a', encoding='utf-8') as f:
            csv_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([title, number_price, date])