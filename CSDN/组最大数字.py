'''
题目描述
给出几组字符串的数字，需要获得组成的最大数字。
比如输入 123， 546， 8， 32，输出 854632123
输入格式：
有多组测试样例，每行包含N个数(每个数不超过1000，空格分开)。

输出格式：
每组数据输出一个表示最大的整数。

示例 1
输入：12 123
输出：12312

示例 2
输入：123 546 8 32
输出：854632123

参考代码

'''
while 1:
    try:
        nums = input().split()

        base = list(range(len(nums)))

        def dfs(val):
            if len(val) == len(nums):
                return int("".join([nums[v] for v in val]))

            for i in base:
                if i not in val:
                    return dfs(val + [i])

        dp = []
        for i in base:
            dp.append(dfs([i]))

        print(max(dp))
    except Exception as e:
        break