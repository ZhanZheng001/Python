'''
题目描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问到达 M 月时有几只兔子。

例如 4 月，有 2 只， 5 月有 3 只，。。。 7 月有 6 只。

输入描述：
输入int型表示month

输出描述：
输出兔子总数int型

示例 1
输入例子:
7
输出例子:
6

参考代码

'''
while 1:
    try:
        month = int(input())
        dp = [1]

        def dfs(n, h):
            if h > month:
                return

            if n > 3:
                dp.append(1)
                dfs(2, h+1)

            dfs(n+1, h+1)

        dfs(1, 1)
        print(sum(dp))
    except Exception as e:
        break