'''
题目描述
公司员工的工号规则为:
小写字母+数字，总长度不能超过8位，x表示该工号类型可以容纳的员工人数，y表示字母的个数，请确定数字的最小个数。

示例 1
输入：260 1
输出：1

示例 2
输入：2600 1
输出：2
'''
while 1:
    try:
        max_, y = list(map(int, input().split()))

        z = 26**y
        for i in range(1, 9-y):
            if z * (10**i) >= max_:
                print(i)
                break

    except Exception as e:
        break
