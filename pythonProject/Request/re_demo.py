import re
import requests

# content = 'Hello,小伙伴们大家好,我是安迪.大熊课堂技术交流群913293727'
# result = re.match('.*?(\d+)',content)
# print(result.group(1))

# url = 'http://localhost/shopxo/?s=goods/index/id/6.html'
url = 'http://localhost/shopxo/'
response = requests.get(url)
html_content = response.text
# regular = '<b class="goods-price" data-original-price="2998.90">(.*?)</b>'
# content = re.search(regular,html_content,re.S)
# print(content.group(1))

#findall

# regular = '<div class="goods-items">(.*?)</p>'
# goods_items = re.findall(regular,html_content,re.S)
# for item in goods_items:
#     item = re.sub('\s+','',item)
#     print(item)

#compile
day1 = '2022-01-11 11:00'
day2 = '2022-01-11 12:00'
day3 = '2022-01-11 13:00'
regular = '\d{2}:\d{2}'
pattern = re.compile(regular)
print(pattern)
print(re.sub(pattern,'',day1))
print(re.sub(pattern,'',day2))
print(re.sub(pattern,'',day3))


