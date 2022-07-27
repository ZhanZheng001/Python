'''
题目描述
在一段路径上，一共有N(N ∈ [1, 100000])座路灯，已知路灯间距均为100m。现给出每个路灯的照亮范围light[i],且照亮范围在区间[1, 100 * N]内。

求出该段路中，总共未照亮的路段长度。
N = 6, light[] = [50,20,80,20,30,300]

示例 1
输入：
6
50,20,80,20,30,300
输出：
30

示例 2
输入：
4
50,70,20,70
输出：
20


'''
# 参考代码
# 以 50,70,20,70 为例
#
# |        |        |        |
# 0        1        2        3
# 1
# 2
# i=0 时 向右侧能照亮50，dp[0] = 50；
# i=1 时 向左侧能照亮70， 向右侧能照亮70 , dp[0] = 50+70, dp[1] = 70;
# i=2 时 向左侧能照亮20， 向右侧能照亮20, dp[1] = 70+20, dp[2] = 20;
# i=3 时 向左侧能照亮70，dp[2] = 20+70;

dp = [100, 90, 90]

while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split(",")))

        dp = [0] * (n-1)

        def funcl(i, w):
            if w > 0 and i >= 0:
                dp[i] = min(100, dp[i] + w)
                funcl(i - 1, w - 100)

        def funcr(i, w):
            if w > 0 and i < n-1:
                dp[i] = min(100, dp[i] + w)
                funcr(i + 1, w - 100)

        for i in range(n):
            funcl(i-1, nums[i])
            funcr(i, nums[i])

        print((n-1)*100 - sum(dp))
    except Exception as e:
        break