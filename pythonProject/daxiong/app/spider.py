import requests
from openpyxl import Workbook
from datetime import datetime
from app.config import BASE_DIR

def get_page(index):
    payload = {
        "activityId": 0,
        "keyword": "python",
        "orderType": 50,
        "pageIndex": index,
        "pageSize": 50,
        "priceType": -1,
        "qualityType": 0,
        "relativeOffset": 0,
        "searchTimeType": -1,
        "searchType": 10
    }
    headers={
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
    url='https://study.163.com/p/search/studycourse.json'
    try:
        response = requests.post(url,headers=headers,json=payload)
        data = response.json()
        if data and data['code']==0:
            return data
    except:
        print('出错了')

def get_course(data):
    course_list = data['result']['list']
    return course_list

def main(index):
    data = get_page(index)
    course_list = get_course(data)
    for course in course_list:
        course_tuple = (
            course['productId'], course['courseId'], course['productName'], course['productType'], course['provider'],
            course['score'], course['scoreLevel'],course['learnerCount'], course['lessonCount'],course['couponPrice'],
            course['originalPrice'], course['discountPrice'], course['vipPrice'],course['imgUrl'],course['bigImgUrl'],
            course['description']
        )
        ws.append(course_tuple)

if __name__=='__main__':
    print('开始爬取,请耐心等待...')
    title = ['productId','courseId','productName','productType','provider',
             'score','scoreLevel','learnerCount','lessonCount','couponPrice',
             'originalPrice','discountPrice','vipPrice','imgUrl','bigImgUrl',
             'description']
    wb = Workbook()
    ws = wb.active
    ws.append(title)
    total_page_count=get_page(1)["result"]["query"]["totlePageCount"]
    total_count = get_page(1)["result"]["query"]["totleCount"]
    print(f'大约有{total_count}条数据')
    for index in range(1,total_page_count+1):
        main(index)
    wb.save(f'{BASE_DIR}\c_excel\网易云课堂python课程信息{datetime.now().strftime("%Y-%m-%d")}.xlsx')
    print('爬取完成')
