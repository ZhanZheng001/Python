from bs4 import BeautifulSoup
import requests
import lxml

def get_page(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    return soup

def get_news_list(url):
    soup = get_page(url)
    news = soup.select('.banner-news ul li a')
    links = []
    for item in news:
        link = item.get('href')
        if link not in ('http://localhost/shopxo/?s=article/category/id/24.html',
                        'http://localhost/shopxo/?s=article/category/id/18.html',
                        'http://localhost/shopxo/?s=article/category/id/17.html'):
            links.append(link)
    return links

def get_news_detail(url):
    soup = get_page(url)
    news_detail = {}
    news_detail['title'] = soup.find('h1', {'class': 'am-article-title'}).string
    news_detail['publish_date'] = soup.select('.am-article-meta span')[0].string
    news_detail['view_count'] = soup.select('.am-article-meta span')[1].string
    news_detail['content'] = soup.find('div', {'class': 'am-article'}).text
    return news_detail

def main():
    links = get_news_list('http://localhost/shopxo/')
    news_list = []
    for link in links:
        news_detail = get_news_detail(link)
        news_list.append(news_detail)
        print(news_detail)
    print(news_list)
if __name__ == '__main__':
    main()


# url = 'http://localhost/shopxo/'
# try:
#     response = requests.get(url)
# except:
#     raise Exception('请求失败')
#
# html_content = response.text
# soup = BeautifulSoup(html_content,'lxml')
# news = soup.select('.banner-news ul li a')
# links=[]
# for item in news:
#     link = item.get('href')
#     if link not in ('http://localhost/shopxo/?s=article/category/id/24.html','http://localhost/shopxo/?s=article/category/id/18.html','http://localhost/shopxo/?s=article/category/id/17.html'):
#         links.append(link)
#
# news_list = []
# for link in links:
#     news_detail = {}
#     soup = BeautifulSoup(requests.get(link).text,'lxml')
#     news_detail['title'] = soup.find('h1',{'class':'am-article-title'}).string
#     news_detail['publish_date'] = soup.select('.am-article-meta span')[0].string
#     news_detail['view_count'] = soup.select('.am-article-meta span')[1].string
#     news_detail['content'] = soup.find('div',{'class':'am-article'}).text
#     news_list.append(news_detail)
# print(news_list)
# for item in news_list:
#     print(item)