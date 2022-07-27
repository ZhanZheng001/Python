'''
题目描述
数字从 1 开始，遇到数字 7 就会跳过，比如 6 后边直接是 8， 69 后边直接是 80，现在给你
个数字，问是第几位？

比如输入 8，输出 7，就是第 7 个数。

示例 1
输入：8
输出：7

这道题和 【华为机试真题 Python实现】计费表故障 是一样的。

参考代码

'''
while 1:
    try:
        num = int(input())

        count = 0
        i = 0
        while i <= num:
            i += 1
            i = int(str(i).replace("7", "8"))
            if i > num:
                break
            count += 1

        print(count)
    except Exception as e:
        break