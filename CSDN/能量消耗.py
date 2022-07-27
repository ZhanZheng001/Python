'''
题目描述
给出一批用户，每个用户有 3 种选择 A\B\C，但是价值不同，相临的用户不能选同一个，求
出所有用户选择后总价值最大。
3 个用户
30 8 4
50 20 9
11 7 6
输出 65，因为选 8 50 7

示例 1
输入：
3
30 8 4
50 20 9
11 7 6

输出：
65

参考代码
思路同 【华为机试真题 Python实现】最优策略组合下的总的系统消耗资源数
一个获取最大值，一个时获取最小值


'''
while 1:
    try:
        n = int(input())
        nums = [list(map(int, input().split())) for _ in range(n)]

        def dfs(idx, com, val):
            # idx 用户id
            # com 三个策略
            # val 资源消耗
            if idx == n - 1:
                return val
            idx += 1
            return max([dfs(idx, c, nums[idx][c]) + val for c in [0, 1, 2] if c != com])

        dp = []
        for c in [0, 1, 2]:
            dp.append(dfs(0, c, nums[0][c]))

        print(max(dp))
    except Exception as e:
        break