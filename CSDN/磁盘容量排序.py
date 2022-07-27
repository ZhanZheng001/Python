'''
题目描述
磁盘的容量单位常用的有有 M， G， T 这三个等级，它们之间的换算关系是 1T=1000G，1G=1000M，现在给定 n 块磁盘的容量，请对它们按从小到大的顺序进行排序，例如给定 3 块盘的容量， 1T， 20M， 3G，排序后的结果未 20M， 3G， 1T

输入描述：
1、每个测试用例第一行包含一个整数 n(2<=n<=1000)，表示磁盘的个数，接下的 n 行，每行一个字符串（长度大于 2，小于 10），表示磁盘的容量，格式为： mv，其中 m 表示
容量大小， v 表示容量单位，例如 20M， 1T， 30G

2、磁盘容量 m 表示十进制数范围为 1 到 1000 的正整数，容量单位 v 的范围只包含题目中提到的 M， G， T 三种，换算关系如题目描述

输出描述：
输出 n 行，表示 n 块磁盘容量排序后的结果

示例 1
输入：

3
1T
20M
3G
1
2
3
4
输出：

20M
3G
1T
1
2
3
示例 2
输入：

3
2G4M
3M2G
1T
1
2
3
4
输出：

20M
3G
1T
1
2
3
参考代码

'''
import re
base = ("\dM", "\dG", "\dT")
def toM(s):
    total = 0
    for i, v in enumerate(base):
        d = re.search(v, s)
        if d:
            total += int(d.group()[:-1]) * 1000 ** i
    return total, s
while 1:
    try:
        n = int(input())
        nums = []
        for _ in range(n):
            # 将磁盘容量 M， G， T 全部转换为 M
            nums.append(toM(input()))
        nums = sorted(nums, key=lambda x: x[0])
        for d in nums:
            print(d[1])
    except Exception as e:
        break