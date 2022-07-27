'''
题目描述
题目描述：勾股数，是由三个正整数组成的数组；能符合勾股定理 aa + bb = c*c ， (a, b, c) 的正整数解。
如果 (a, b, c) 是勾股数，它们的正整数倍数，也是勾股数。
如果 (a, b, c) 互质，它们就称为素勾股数。
给定正整数 N， 计算出小于或等于 N 的素勾股数个数。

输入描述：
输一个正整数

输出描述：
素勾股数

示例 1
输入：10
输出：1
'''
def ac(a, b): # 返回最大公约数
    mod = 2  # 随便定义一个余数
    while mod != 0:  # 当余数等于0是最大公约数
        mod = a % b
        a = b
        b = mod
    return a
while 1:
    try:
        m = int("20")
        dp = []
        for a in range(m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    if a * a + b * b == c * c and ac(a, b) == ac(b, c) == ac(a, c) == 1: # 互质 最大公约数为1
                        dp.append((a, b, c))
        print(len(dp))
        break
    except Exception as e:
        break