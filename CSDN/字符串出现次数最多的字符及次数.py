'''
题目描述
统计数字出现的次数，最大次数的统计出来举例：
输入： 323324423343
输出： 3,6

示例 1
输入： 323324423343
输出： 3,6

参考代码
统计出现最多字符的可以使用哈希表来存储；
由于输入是一个由数字组成的字符串，所以可以考虑使用列表；
声明一个长度为10的列表，下标是需要统计的数字，元素是出现的次数；


'''
while 1:
    try:
        nums = list(map(int, list(input())))

        dp = [0] * 10
        for n in nums:
            dp[n] += 1

        max_ = max(dp)
        print(f"{dp.index(max_)},{max_}")
    except Exception as e:
        break