'''
题目描述
给定一个没有重复数字的序列，返回其所有可能的全排列。

输入描述：
输入:[1,2,3]

输出描述：
输出:[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 1
输入：

1,2,3
1
输出：

[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
1

'''
# 参考代码
# 方法一：
# 排列组合可以使用 itertools 库；
#
# permutations 作用：返回指定长度的排列；
# combinations作用：返回指定长度的组合；
# combinations_with_replacement作用：返回指定长度的组合，组合内元素可重复。
import itertools


while 1:
    try:
        nums = list(map(int, input().split(",")))
        print([list(i) for i in itertools.permutations(nums, len(nums))])
    except Exception as e:
        break

# 方法二：
# 递归求解

while 1:
    try:
        nums = list(map(int, input().split(",")))
        dp = []

        def dfs(s):
            if len(s) == len(nums):
                dp.append(s)
            else:
                for c in nums:
                    if c not in s:
                        dfs(s + [c])


        for c in nums:
            dfs([c])

        print(dp)
    except Exception as e:
        break