import random
from tools.cal_time import *

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1): #第i趟
        exchange = False #添加标志,如果某一趟没有变更,则代表已经排序好了,直接返回
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        if not exchange:
            return
        # print(li)

# li = [1,2,3,6,5,4,7,9,8]
li = list(range(10000))
random.shuffle(li)
bubble_sort(li)