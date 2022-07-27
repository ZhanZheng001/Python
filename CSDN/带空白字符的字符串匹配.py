'''
题目描述
给定两行空的字符串，第一行的字符串包含了部分空白（空格、 tab），第二行字符串不包含任何空白，请从第一行字符串中匹配第二行字符串，匹配时忽略空白及 tab，输出
第一行字符串中第二行字符串出现的次数；

输入描述：
第一行输入小于 1K 的字符串，包含了部分空白（空格、 tab）
第二行输入小于 1K 的字符串，不包含任何空白

输出描述：
输出匹配到的次数（如果遇到连续字符如 bbb,查找 bb,记为匹配两次）

示例 1
输入：

Abb ba
bb
1
2
输出：
2

参考代码

'''
while 1:
    try:
        nums = input().replace(" ", "").replace("\t", "")
        sub = input()

        count = 0
        while len(nums):
            if sub in nums:
                i = nums.index(sub)
                nums = nums[i+1:]
                count += 1
            else:
                break

        print(count)
    except Exception as e:
        break