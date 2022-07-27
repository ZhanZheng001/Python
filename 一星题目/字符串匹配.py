'''
给出一个字符串，给出一个正则白表达式子串，找出可以找到子串的第一个位置。
例如:字符串 asdfas，子串是 d[sf]，（[]表示里边任意一个元素），输出为 3，因为 ds 或 df 去匹配字符串，找到 df 输出位置为 3。
输入描述：
输入第一行是字符串m，第二行是子串k
输出描述：
输出子串第一次出现的位置
示例 1
输入：
asdfas
d[sf]
输出：
3
'''
import re
while 1:
    try:
        m = "asdfas"
        k = "d[sf]"
        a = re.search(k, m)
        print(a.span()[0]+1) if a else print(-1)
        break
    except Exception as e:
        break