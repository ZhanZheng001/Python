'''
题目描述
入职后，导师会请你吃饭，你选择了火锅。

火锅里会在不同时间下很多菜。

不同食材要煮不同的时间，才能变得刚好合适。你希望吃到最多的刚好合适的菜，但你的手速不够快，用m代表手速，每次下手捞菜后至少要过m庙才能在捞（每次只能捞一个）。

那么用最合理的策略，最多能吃到多少刚好合适的菜？

输入描述：
第一行两个整数n，m，其中n代表往锅里下的菜的个数，m代表手速。
接下来有n行，每行有两个数x，y代表第x秒下的菜过y秒才能变得刚好合适。
（1 < n, m < 1000）
（1 < x, y < 1000）

输出描述：
输出一个整数代表用最合理的策略，最多能吃到刚好合适的菜的数量

示例 1
输入：
2 1
1 2
2 1

输出：
1

参考代码
1 2
2 1
菜熟的时间可以转换成时间轴 0 0 2 ，因为一个时刻只能捞一个 可以表示为 0 0 1，一个时刻也可以简化为 捞或者不捞 。
'''
while 1:
    try:
        n, m = list(map(int, input().split()))

        idx = []
        for _ in range(n):
            i, v = list(map(int, input().split()))
            idx.append(i+v)

        nums = [0] * (max(idx)+1)
        for i in idx:
            nums[i] = 1

        dp = []

        def dfs(t, data):
            # t 可以夹菜的时间, 因为每秒夹一次，也可作为时间轴
            if t >= len(nums):
                dp.append(sum(data))
                return
            # 等于 1 此时有菜，但是可以选择吃或者不吃，可能会影响后面夹菜的顺序
            if nums[t] == 1:
                # 1 表示吃，吃了要直接跳到m秒后
                # 没吃 过1s继续选择 吃或者不吃
                dfs(t+m, data + [1])
                dfs(t+1, data)
            else:
                dfs(t+1, data)

        dfs(1, [])

        print(max(dp))
    except Exception as e:
        break