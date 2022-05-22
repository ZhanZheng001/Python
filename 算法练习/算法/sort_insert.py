import random
from tools.cal_time import *

@cal_time
def insert_sort(li):
    for i in range(1,len(li)): #i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1 # j表示手里的牌的下标
        while j >= 0 and li[j]> tmp:
            li [j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        # print(li)

# li = [3,2,4,1,5,6,8,7,9]
li = list(range(10000))
random.shuffle(li)
insert_sort(li)