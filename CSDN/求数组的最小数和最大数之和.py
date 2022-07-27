'''
题目描述
题目大概是输入整型数组求数组的最小数和最大数之和，另外数组的长度不超过 50。

示例 1
输入：1,2,3,4
输出：5

示例 2
输入：1
输出：2

当输入只有一个数的时候，则最小数和最大数都是该数

参考代码

'''
while 1:
    try:
        nums = list(map(int, input().split(",")))
        print(min(nums) + max(nums))
    except Exception as e:
        break