from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import re
import time

words = []
url = 'URL' # Put URL here

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# From here on, this is specific for the URL I used. This can get tricky (like here).
# Often times, you can get away with a simple
# soup.findAll('div', {'class': 'value'}).findAll('p').getText()
first_word = soup.findAll('div', {'class': 'col-lg-3 col-md-4 col-sm-6 col-xs-12 bottom-buffer'})
words.append(first_word[0].find('p').getText())
for content in soup.contents[3:-24]:
    words.append(str(content))
time.sleep(60) # Be responsible with your number of requests.

# Get rid of leftover HTML
words = [w.replace('<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 bottom-buffer"><p>', '') for w in words]
words = [w.replace('</p></div>', '') for w in words]
# Replace ß by ss, filter by length
words = [w.replace('ß', 'ss') for w in words]
words_extra = [w for w in words if len(w)==3]
words = [w for w in words if len(w)==2]

with open('words_2_characters.json', 'w', encoding='utf-16') as f:
    json.dump(words, f, ensure_ascii=False, indent=4)

with open('words_3_characters_extra.json', 'w', encoding='utf-16') as f:
        json.dump(words_extra, f, ensure_ascii=False, indent=4)