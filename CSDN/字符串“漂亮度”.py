'''
题目描述
给出一个名字，该名字有 26 个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。

每个字母都有一个“漂亮度”，范围在 1 到 26 之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。

给出多个名字，计算每个名字最大可能的“漂亮度”。

示例 1
输入：

zhangsan
lisi
1
2
输出：

192
101
1
2
参考代码
字母的漂亮度是按出现次数来决定大小时，计算的名字漂亮度是最大的；
我们首先生成一个26-1的列表方便后面计算漂亮度；
然后 使用哈希表 存储每个字幕的出现次数；
按出现次数对字典进行排序，排序后返回由 key,value 的元祖构成的 数组；
遍历数组，通过下标获取当前字母的 漂亮值*出现次数；
累加就是名字漂亮度；


'''
counts = list(range(26, 1, -1))
while 1:
    try:
        dp = {}
        for c in input().lower():
            if c in dp:
                dp[c] += 1
            else:
                dp[c] = 1

        dp = sorted(dp.items(), key=lambda x: x[1], reverse=True)
        total = 0
        for idx, val in enumerate(dp):
            total += counts[idx] * val[1]

        print(total)
    except Exception as e:
        break