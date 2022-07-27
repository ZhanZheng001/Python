'''
题目描述
给出母串和子串，输出子串能够在母串完全匹配的开始位置。
比如 asdfasdfa， fas 输出 3，就是最小下标。

输入描述：
第一行是母串
第二行是子串

输出描述：
输出子串能够在母串完全匹配的开始位置。

示例 1
输入：asdfasdfa
输出：fas

参考代码

'''
while 1:
    try:
        a = input()
        b = input()
        if b in a:
            print(a.index(b))
        else:
            print(-1)
    except Exception as e:
        break