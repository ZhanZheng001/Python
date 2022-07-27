'''
A,B两个人把苹果分为两堆，A希望按照它的计算规则等分苹果，他的计算规则是按照二进制加法计算，并且不计算走位，12+5=9（1100+0101=9），
B的计算规则是十进制加法，包括正常进位，B希望在满足A的情况下获取苹果重量最多，输入苹果的数量和每个苹果重量，输出满足A的情况下获取的苹果总重量，
如果无法满足A的要求，输出-1。

输入描述：
输入第一行是苹果数量：3
输入第二行是每个苹果重量：3 5 6

输出描述：
输出第一行是B获取的苹果总重量：11

示例 1
输入：
3
3 5 6
输出：
11

示例 2
输入：
8
7258 6579 2602 6716 3050 3564 5396 1773
输出：
35165
'''
while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        max_ = sum(nums)

        dp = []

        def get_w(sub):
        	# 按照二进制加法计算，并且不计算走位， 计算重量
            t = 0
            for n in set(nums).difference(sub):
                # 按照二进制加法计算
                t = t ^ n
            return t

        def dfs(w, sub):
        	# w 是已经分过得(A)，按照二进制加法计算的重量
        	# sub 是未分配的苹果 (B)
            if w == get_w(sub):
                tot = sum(sub)
                # 取最大实际重量 保存在 dp
                dp.append(max(tot, max_ - tot))
                return
            elif len(sub) == len(nums) - 1:
                # 不能把苹果全部分给 某一堆
                return
            else:
                # 生成可能的 堆组合，计算进行重量比较
                for wi in nums:
                    if wi not in sub:
                        dfs(w ^ wi, sub.union({wi}))

        for w in nums:
            dfs(w, {w})

        if dp:
            print(max(dp))
        else:
            print(-1)
    except Exception as e:
        break