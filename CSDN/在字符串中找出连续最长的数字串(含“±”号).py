'''
题目描述
请在一个字符串中找出连续最长的数字串，并返回这个数字串。

如果存在长度相同的连续数字串，返回最后一个。如果没有符合条件的字符串，返回空字符串""。

注意：

数字串可以由数字"0-9"、小数点"."、正负号"±"组成，长度包括组成数字串的所有符号。 “.”、“± "仅能出现一次，” ."的两边必须是数字， "±"仅能出现在开头且其后必须要有
数字。

长度不定，可能含有空格。

示例1
输入：

1234567890abcd9.+12345.678.9ed
1
输出：

+12345.678
1
解释：
包含的数字串有 1234567890、9、+12345.678、678.9
其中 1234567890、+12345.678 一样长，输出最后一个
+12345.678 和 678.9 这里需要注意，如果 678.9 的 9后面还有数字，他可能是更长的，我们就需要考虑 对前一个数字计算结束后退到前一个 分隔符的情况。


'''
# 参考代码
# 考虑使用两个游标，i，j，当 s[i:j] 还是一个有效数的时候 j++ , 当不满足时计算长度，当遇到 . （小数点）的时候，计算当前的 s[i:j] 并且把 s[j:] 当做一个新字符串，重复以上操作。
#
# 简直了，完全没有算法可言，硬编。

while 1:
    try:

        nums = input()
        dp = []
        cache = []

        def format_(s):
            if s:
                # 去除小数点在末尾的情况  例如 9.
                if s[-1] == ".":
                    dp.append("".join(s[:-1]))
                else:
                    dp.append("".join(s))

        def dfs(s):
            # 减少重复计算
            if s in cache:
                return
            else:
                cache.append(s)

            temp = []
            for i, c in enumerate(s):
                if "0" <= c <= "9":
                    temp.append(c)
                # 在数字串首的 +- 号
                elif c in "+-" and not temp:
                    temp.append(c)
                # 连续出现两次 小数点
                elif c == ".":
                    if c in temp:
                        format_(temp)
                        temp = []
                    elif temp:
                        temp.append(c)
                        dfs(s[i+1:])
                else:
                    format_(temp)
                    temp = []

            format_(temp)

        dfs(nums)

        max_ = ""
        for lst in dp:
            if len(max_) <= len(lst):
                max_ = lst

        print(max_)
    except Exception as e:
        break