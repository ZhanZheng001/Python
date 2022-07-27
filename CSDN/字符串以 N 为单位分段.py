'''
题目描述
输入 m 个字符串和一个整数 n, 把字符串 M 化成以 N 为单位的段，不足的位数用 0 补齐。

如 m=2 n=8
123456789 划分为： 12345678,90000000
123 划化为： 12300000

示例 1
输入：
2 8
abc 123456789

输出：
abc00000
12345678,90000000


'''
# 参考代码

while 1:
    try:
        m, n = list(map(int, input().split()))
        nums = input().split()

        for c in nums:
            print(",".join([c[i: i+n].ljust(n, "0") for i in range(0, len(c), n)]))

    except Exception as e:
        break

# 可以拆解为
for c in nums:
    dp = []
    for i in range(0, len(c), n):
        dp.append(c[i: i+n].ljust(n, "0"))

    print(",".join(dp))

# 如果忘记右侧补充可以使用字符串截取
for c in nums:
    dp = []
    for i in range(0, len(c), n):
        dp.append(f"{c[i: i+n]}{'0'*n}"[:n])
    print(",".join(dp))