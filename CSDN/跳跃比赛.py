'''
题目描述
给出一组正整数，你从第一个数向最后一个数方向跳跃，每次至少跳跃 1 格，每个数的值表示你从这个位置可以跳跃的最大长度。计算如何以最少的跳跃次数跳到最后一个数。

输入描述：
第一行表示有多少个数 n
第二行开始依次是 1 到 n 个数，一个数一行

输出描述：
输出一行，表示最少跳跃的次数。

示例 1
输入：
7
2 3 2 1 2 1 5
输出：
3

解释：
从下标 0->1->4->6，跳跃3次；
从下标 0->2->4->6，跳跃3次；

参考代码

'''
def dfs(nums, i=0):
    if len(nums) <= i+1:
        return 0

    return min([dfs(nums, i+j)+1 for j in range(1, nums[i]+1)])


while 1:
    try:
        _ = input()

        nums = list(map(int, input().split()))

        print(dfs(nums))
    except Exception as e:
        break