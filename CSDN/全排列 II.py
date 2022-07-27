'''
题目描述
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

输入描述：
输入:[1,2,3]

输出描述：
输出:[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 1
输入：

1,1,2
1
输出：

[[1,1,2],
[1,2,1],
[2,1,1]]
1
2
3
示例 2
输入：

1,1,2
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
        print([list(i) for i in set(itertools.permutations(nums, len(nums)))])
    except Exception as e:
        break

# 方法二：

while 1:
    try:
        nums = list(map(int, input().split(",")))

        base = [i for i in range(len(nums))]
        base_dp = []

        def dfs(s):
            if len(s) == len(nums):
                base_dp.append(s)
            else:
                for c in base:
                    if c not in s:
                        dfs(s + [c])

        for c in base:
            dfs([c])

        dp = []
        for i in base_dp:
            temp = [nums[j] for j in i]
            if temp not in dp:
                dp.append(temp)

        print(dp)
    except Exception as e:
        break