'''
题目描述
题目描述： 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
输入只有一行，包含一个字符串 S， S 中只包含小写字母
输出不含有重复字符的最长子串的长度

示例1
输入：

abcabcbb
1
输出：

3
1
解释: 因为无重复字符的最长子串是 “abc”，所以其长度为 3。

示例 2:
输入：

bbbbb
1
输出：

1
1
解释: 因为无重复字符的最长子串是 “b”，所以其长度为 1。

示例 3:
输入：

pwwkew
1
输出：

3
1
解释: 因为无重复字符的最长子串是 “wke”，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，“pwke” 是一个子序列，不是子串。

参考代码

'''
while 1:
    try:
        s = input()
        dp = 1 if s else 0
        n = len(s)
        i = 0
        j = 1
        while i < n:
            while j < n:
                if s[j] in s[i:j]:
                    dp = max(j - i, dp)
                    i = i + s[i:j].index(s[j])
                    j += 1
                    break
                else:
                    dp = max(j + 1 - i, dp)
                    j += 1
            i += 1
        print(dp)
    except Exception as e:
        break