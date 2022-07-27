'''
题目描述
微商模式比较典型，下级每赚 100 元就要上交 15 元，给出每个级别的收入，求出金字塔尖
上的人收入。
比如：
（代理商代号） （上级代理商代号） （代理商转的钱）
1 0 223
2 0 323
3 2 1203
输出是
0（金字塔顶代理商）
105 （最终的钱数）

解释：
2 的最终收入等于 323 + 1203//100 *15 == 323 +180
0 的最终收入等于 (323 +180 + 223)//100 *15 == 105

参考代码
申请一个长度n+1的数组，保存下级对上级上交的收入，存储在上级对应的下标中。


'''
while 1:
    try:
        n = int(input())

        nums = [list(map(int, input().split())) for _ in range(n)]

        nums = sorted(nums, key=lambda x: x[1], reverse=True)

        dp = [0] * (n + 1)
        start = 0
        end = 0
        for i, j, m in nums:
            end = max(i, end)
            start = min(j, start)
            dp[j] += ((m + dp[i])//100) * 15

        print(f"{start} {dp[start]}")
    except Exception as e:
        break