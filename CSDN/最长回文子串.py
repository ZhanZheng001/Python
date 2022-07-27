'''
题目描述
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：babad
输出：bab
解释：“aba” 同样是符合题意的答案。

示例 2：
输入：cbbd
输出：bb
'''
# 参考代码
# 方法一：
# 这个思路比较简单，但是会超时😂😂😂；
# 先看下思路吧；
# 首先我们需要确定一个子串的范围，然后判断当前子串是不是 回文子串；
# 什么是回文子串？
# 就是字符串本身 和 反正后的字符串是相同的，例如 abcddcba。

while 1:
    try:
        s = input()
        lens = len(s)
        dp = []
        for i in range(lens):
            j = i + 1
            while j <= lens:
                if s[i:j] == s[i:j][::-1]:
                    dp.append(s[i:j])
                j += 1

        dp = sorted(dp, key=lambda x: len(x), reverse=True)
        print(dp[0])
    except Exception as e:
        break

# 方法二：
# 中心扩散，从每一个位置出发，向两边扩散即可。遇到不是回文的时候结束。
# 首先往左寻找与当期位置相同的字符，直到遇到不相等为止。
# 然后往右寻找与当期位置相同的字符，直到遇到不相等为止。

while 1:
    try:
        s = input()
        n = len(s)
        if n < 2:
            print(s)
            break

        max_len = 0
        start_index = 0

        def hw_len(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1, left + 1

        # 中心扩散法
        for i in range(0, n-1):
            # 单核心
            len1, start_index1 = hw_len(i, i)
            # 双核心
            len2, start_index2 = hw_len(i, i+1)

            if len1 > max_len:
                max_len = len1
                start_index = start_index1
            if len2 > max_len:
                max_len = len2
                start_index = start_index2

        print(s[start_index: start_index+max_len])
    except Exception as e:
        break