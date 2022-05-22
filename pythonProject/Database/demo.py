from bs4 import BeautifulSoup
import requests
import lxml

url = "http://localhost/shopxo/"
try:
    response = requests.get(url)
except:
    raise Exception('请求失败')

html_content = response.text
soup = BeautifulSoup(html_content,'lxml')
print(soup)