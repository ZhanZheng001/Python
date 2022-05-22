import requests
import lxml
from pyquery import PyQuery as pq

url = 'http://localhost/shopxo/'
response = requests.get(url)
html_content = response.text
doc = pq(html_content)

print(doc('.goods-list').children())