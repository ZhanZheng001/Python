'''
题目描述
将第一行中含有第二行中“23”的数输出并排序
输入一行数字： 123 423 5645 875 186523
在输入第二行： 23

将第一行中含有第二行中“23”的数输出并排序结果即： 123 423 186523

示例 1
输入：123 423 5645 875 186523
输出：123 423 186523

参考代码

'''
while 1:
    try:
        nums = input().split()
        key = input()

        dp = []
        for word in nums:
            if key in word:
                dp.append(word)

        print(" ".join(dp))
    except Exception as e:
        break