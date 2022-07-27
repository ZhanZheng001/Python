'''
题目描述
给定一个数组，从第一个开始，正好走到数组最后，所使用的最少步骤数。

要求：
第一步从第一元素开始，第一步小于<len/2（len 为数组的长度）。从第二步开始，只能以所在成员的数字走相应的步数，不能多也不能少, 如果目标不可达返回-1，输出最少的步骤数，不能往回走。

示例 1
输入：7 5 9 4 2 6 8 3 5 4 3 9
输出：2

示例 2
输入：1 2 3 7 1 5 9 3 2 1
输出：-1

参考代码

'''
while 1:
    try:
        nums = list(map(int, input().split()))

        def dfs(n, c):
            if n == len(nums) - 1:
                return c
            elif n < len(nums):
                return dfs(n+nums[n], c+1)

        dp = []
        for i in range(len(nums)//2):
            t = dfs(i, 1)
            if t:
                dp.append(t)

        if dp:
            print(min(dp))
        else:
            print(-1)
    except Exception as e:
        break