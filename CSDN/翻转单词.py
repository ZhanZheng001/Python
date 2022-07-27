'''
题目描述
给一个由英文单字和空格组成的字符串，如：I am a student ,翻转[1 3]之间的单词，即得：I student a am .
n是翻转得下标，n,m给定的，如果n小于0,则从下标为0开始翻转，如果m大于等于字符转单词下标，则翻转到最后一个单词。

输入描述：
第一行是待处理的字符串
第二行翻转下标n, m
输出描述：
输出翻转后的字符串

示例 1
输入：
I am a boy she is girl
-1 4
输出：
she boy a am I is girl
'''
while 1:
    try:
        s = "I am a boy she is girl".split()
        n, m = list(map(int, "-1 4".split()))
        if n >= m:
            print(s)
        else:
            if n < 0:
                n = 0
            if m > len(s):
                m = len(s) - 1
            s0 = s[:n]
            s1 = s[n:m+1]
            s2 = s[m+1:]
            print(" ".join(s0 + s1[::-1] + s2))
            break
    except Exception as e:
        break
