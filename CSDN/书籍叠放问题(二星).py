'''
题目描述
假设书本的叠放有这样的规则，当A书的长度和宽度都大于B书时，可以将其B书置于A的上方，堆叠摆放，请设计一个程序，根据输入的书本长宽，计算最多可以堆叠摆放多少本书？

示例 1
输入：
3
16 15
13 12
15 14

输出：
3

说明
这里代表有3本书，第1本长宽分别为16和15，第2本长宽为13和12，第3本长宽为15和14，它们可以按照 [13, 12],[15, 14],[16,15] 的顺序堆叠，所以输出3

参考代码

'''
while 1:
    try:
        n = int(input())

        nums = [list(map(int, input().split())) for _ in range(n)]

        dp = []
        lens = len(nums)

        def dfs(sub, count=1):
            if count >= lens:
                dp.append(len(sub))
            else:
                for i in range(lens):
                    if i not in sub:
                        if nums[i][0] < nums[sub[-1]][0] and nums[i][1] < nums[sub[-1]][1]:
                            dfs(sub+[i], count+1)

        for i in range(lens):
            dfs([i])

        print(max(dp))
    except Exception as e:
        break