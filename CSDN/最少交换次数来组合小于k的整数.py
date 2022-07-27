'''
题目描述
给出数字k,请输出所有结果小于k的整数组合到一起的最小交换次数。 组合一起是指满足条件的数字相邻，不要求相邻后在数组中的位置。

数据范围 -100 <= k <= 100 -100 <= 数组中的值 <= 100

示例 1
输入：
1 3 1 4 0
2
输出： 1

示例 2
输入：
0 0 1 0
2
输出： 0

示例 3
输入：
2 3 2
1
输出： 0

参考代码
将大于等于k的置为0，小于k的置为1；
1 3 1 4 0 转换后 1 0 1 0 1
一共有3个小于k的数，确定宽度为3的窗口向右滑动，窗口中1的数量越多移动的次数越少。


'''
while 1:
    try:
        nums = list(map(int, input().split()))
        k = int(input())

        for i in range(len(nums)):
            if nums[i] < k:
                nums[i] = 1
            else:
                nums[i] = 0

        n = len(nums)
        m = sum(nums)

        dp = []
        for i in range(n):
            dp.append(sum(nums[i: i+m]))

        print(m-max(dp))
    except Exception as e:
        break