'''
题目描述
某计费表有故障，凡任意数字位置遇到数字4就直接跳过，
输入一个数代表计费表的度数，输出一个数代表实际读数

示例 1
输入：5
输出：4

示例 2
输入：17
输出：15

示例 3
输入：100
输出：81

参考代码
模拟题


'''
while 1:
    try:
        num = int(input())

        count = 0
        i = 0
        while i <= num:
            i += 1
            i = int(str(i).replace("4", "5"))
            if i > num:
                break
            count += 1

        print(count)
    except Exception as e:
        break