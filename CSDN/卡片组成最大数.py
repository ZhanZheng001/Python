'''
题目描述
小组中每位都有一张卡片，卡片上是 6 位内的正整数，将卡片连起来可以组成多种数字，计算组成的最大数字。

输入描述：
“,”号分割的多个正整数字符串，不需要考虑非数字异常情况，小组最多 25 个人
输出描述：
最大的数字字符串

示例 1
输入：

22,221
1
输出：

22221
1
参考代码
对字符串分割，求解所有的组个，按组拼接字符串产生新的数组，对数组排序。


'''
while 1:
    try:
        nums = input().split(",")

        dp = []

        def dfs(s):
            if len(s) == len(nums):
                dp.append("".join(s))
            else:
                for c in nums:
                    if c not in s:
                        dfs(s + [c])

        for c in nums:
            dfs([c])

        dp = sorted(dp, reverse=True)
        print(dp[0])
    except Exception as e:
        break