'''
题目描述
给你一个数可以分解成几组的连续的自然数之和？
比如 8 可以分解成 8，即 1 组
比如 6 可以分解成 6,123，即 2 组。

输入描述：
输入一个整数

输出描述：
输出可以分解的组数

示例 1
输入：8
输出：1

示例 2
输入：6
输出：2

参考代码
从题目给出的示例来看，每个数默认有一组可能，就是数值本身；
n本身 一些题里数值本身应该是不算一种可能的；
n = 0 + n, 除了 n=1 其他数都不是连续的。



'''
while 1:
    try:
        num = int(input())

        dp = [[num]]


        def dfs(n):
            total = sum(n)
            if total == num:
                dp.append(n)
            elif total > num:
                return
            else:
                dfs(n + [n[-1] + 1])


        for i in range(1, (num // 2 + 1)):
            dfs([i])

        print(len(dp))
    except Exception as e:
        break