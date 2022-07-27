'''
题目描述
给定一个 M 行 N 列的矩阵（M*N 个格子），每个格子中放着一定数量的平安果。
你从左上角的各自开始，只能向下或者向右走，目的地是右下角的格子。
每走过一个格子，就把格子上的平安果都收集起来。求你最多能收集到多少平安果。

注意：当经过一个格子时，需要一次性把格子里的平安果都拿走。

限制条件： 1<N,M<=50；每个格子里的平安果数量是 0 到 1000（包含 0 和 1000） .

输入描述：
输入包含两部分：
第一行 M, N
接下来 M 行，包含 N 个平安果数量

输出描述：
一个整数 ， 最多拿走的平安果的数量

示例 1
输入：
2 4
1 2 3 40
6 7 8 90

输出：
136

参考代码
递归解法 可参考 【华为机试真题 Python实现】机器人走迷宫


'''
while 1:
    try:
        m, n = list(map(int, input().split()))

        nums = [list(map(int, input().split())) for _ in range(m)]

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = nums[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + nums[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + nums[i][j]
                else:
                    dp[i][j] = max((dp[i-1][j], dp[i][j-1])) + nums[i][j]
        print(dp[-1][-1])
    except Exception as e:
        break