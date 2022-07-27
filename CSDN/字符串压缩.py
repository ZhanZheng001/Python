'''
题目描述
通过键盘输入一串小写字母(a~z)组成的字符串。请编写一个字符串压缩程序， 将字符串中连续出席的重复字母进行压缩，并输出压缩后的字符串。

压缩规则：

仅压缩连续重复出现的字符。比如字符串"abcbc"由于无连续重复字符，压缩后的字符串还是"abcbc".
压缩字段的格式为"字符重复的次数+字符"。例如：字符串"xxxyyyyyyz"压缩后就成为"3x6yz"
示例1:
输入：

aabcccccaaa
1
输出：

2ab5c3a
1
示例2:
输入：

abbccd
1
输出：

a2b2cd
1
示例 3:
输入：

IIIIeeeeOODDDssppppooQQQQppplllhU
1
输出：

4I4e2O3D2s4p2o4Q3p3lhU
1
参考代码

'''
while 1:
    try:
        S = input()
        if not S:
            print(S)
            break

        dp = ""
        i = 0
        j = 1
        while j < len(S):
            if S[i] != S[j]:
                if j - i > 1:
                    dp += str(j - i)
                dp += S[i]
                i = j
            j += 1

        if j - i > 1:
            dp += str(j - i)
        dp += S[i]
        print(dp)
    except Exception as e:
        import traceback
        print(traceback.print_exc())
        break