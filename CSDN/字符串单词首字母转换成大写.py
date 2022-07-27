'''
题目描述
字符串单词首字母转换成大写。

示例 1
输入：this is a book
输出：This Is A Book

参考代码

'''
while 1:
    try:
        nums = input().split()

        dp = [f"{w[0].upper()}{w[1:]}" for w in nums]

        print(" ".join(dp))
    except Exception as e:
        break