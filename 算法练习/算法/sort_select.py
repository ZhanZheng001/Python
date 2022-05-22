import random
from tools.cal_time import *

@cal_time
def select_sort_simple(li): #不推荐该方法,复杂度高
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

@cal_time
def select_sort(li):
    for i in range(len(li)-1): #第i趟
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]
        # print(li)



# li = [3,2,4,1,5,6,8,7,9]

li = list(range(10000))
random.shuffle(li)
select_sort(li)