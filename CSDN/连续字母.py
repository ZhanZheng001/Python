'''
题目描述
给你一个字符串，只包含大写字母，求同一字母连续出现的最大次数。

例如”AAAABBCDHHH”，同一字母连续出现的最大次数为 4，因为一开始 A 连续出现了 4 次。

输入描述：
输入一个子串(1<长度<=100)。

输出描述：
输出对应每个子串同一字母连续出现的最大次数。

示例 1
输入： AAAABBCDHHH
输出： 4

参考代码

'''
while 1:
    try:
        nums = input()

        dp = [1]
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                dp[-1] += 1
            else:
                dp.append(1)

        print(max(dp))
    except Exception as e:
        break