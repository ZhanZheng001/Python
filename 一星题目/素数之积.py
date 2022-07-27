'''
RSA加密算法在⽹络安全世界中⽆处不在，它利⽤了极⼤整数因数分解的难度，数据越⼤，安全系数越⾼，给定⼀个32位整数，请对其进⾏因数分解，找出是哪两个素数的乘积。
示例 1
输入：8633
输出：89 97
'''
dp = {}
def func(n):
    if n <= 1: # 判断是否是素数
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    dp[n] = True
    return True

while 1:
    try:
        num = int("8633")
        for i in range(2, num//2):
            c = num // i
            if c >= i and c*i == num and func(c) and func(i):
                print(f"{i} {c}")
                break
        else:
            print(-1)
        break
    except Exception as e:
        break