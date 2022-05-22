from tools.cal_time import *

@cal_time
def linear_search(li,val):
    for k,v in enumerate(li):
        if v == val:
            return k
        else:
            return None
@cal_time
def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = list(range(100000000))
linear_search(li,899990)
binary_search(li,899990)