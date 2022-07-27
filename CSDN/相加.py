'''
题目描述
华老师让你们计算一个等式， s=a+aa+aaa+aaaa+aa…a(总共有 n 个这样的数相加)的值，其中 a 是一个 1～9 的数字。
例如当 a＝2， n＝5 时， s＝2+22+222+2222+22222。

输入描述：
输入一行包含两个整数 a(1<=a<=9)和 n(1<=n<=9)，其中 n 为几个这样的数字相加（如描述中的例子 n 是 5）。 a 和 n 用空格隔开

输出描述：
输出一个符合题目算法的结果 s。

示例 1
输入： 2 5
输出： 24690

参考代码

'''
while 1:
    try:
        a, n = input().split()

        total = 0
        for i in range(1, int(n)+1):
            total += int(a*i)

        print(total)
    except Exception as e:
        break