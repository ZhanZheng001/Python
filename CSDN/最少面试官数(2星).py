'''
题目描述
公司正在组织集中面试，每场面试需要一个面试官，现在以数组的形式给出了每场面试的开始时间和结束时间的时间安排表 [si, ei] (si < ei)），
为避免面试冲突，请问至少需要多少位面试官，才能满足这些面试安排。

示例 1
输入:
3
0 30
5 10
15 20
输出: 2

示例 2
输入:
2
7 10
2 4
输出: 1

参考代码
我们模拟有一条时间线，当有面试时 时间线上的范围 +1；
时间线上最大数值就是需要的面试官数；


'''
while 1:
    try:
        n = int(input())

        nums = []
        for _ in range(n):
            nums.append(list(map(int, input().split())))

        nums = sorted(nums, key=lambda x: x[0])
        max_ = max([e for s, e in nums])

        dp = [0] * (max_+1)

        for s, e in nums:
            for i in range(s, e+1):
                dp[i] += 1

        print(max(dp))
    except Exception as e:
        break