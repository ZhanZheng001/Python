'''
题目描述
输入一串字符，只包含“0-10”和“， ”找出其中最小的数字和最大的数字（可能不止一个），输出最后剩余数字个数。

示例 1
输入：3,3,4,5,6,7,7
输出：3

参考代码

'''
while 1:
    try:
        nums = list(map(int, input().split(",")))
        print(len(nums) - nums.count(min(nums)) - nums.count(max(nums)))
    except Exception as e:
        break