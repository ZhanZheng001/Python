'''
题目描述：
给定一个无重复元素的数组和一个目标数 target，找出数组中所有可以使数字和为 target 的组合。

数组中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

示例 1：
输入：
5,3,6,7 9
1
输出：
[[3,3,3],[3,6]]
1
示例 2：
输入：
2,3,6,7 7
1
输出：
[[7],[2,2,3]]
1
参考代码
我们来分析下示例1，数组 [5,3,6,7] 和 target 9 ，目的是要取数组中的组合起来等于 9；
我们先确定第一个值 5，5 小于 9 需要再找一个数组合；
9 和 5 差值是 4，我们下一步就是再找到可以组合出 4 的值，这里又回到了和找 9 的方法一样了；
在数组中小于等于 4 的值只有 3，我们确定第二个值 3；
下轮要找小于等于 1 的值，数组中没有，那这个组合就不满足要求；
按这个思路我们可以使用递归， 对每次产生的差值缩小范围继续查找组合得到最终结果；
可以发现 当我们找差值时，如果数组时有序的，比较前面的值已经不满足要求，就可以不用计算后面更大的值了。


'''
while 1:
    try:
        nums, target = input().split()
        target = int(target)
        nums = list(map(int, nums.split(",")))
        nums = sorted(nums)

        ret = set()

        def dfs(tge, data):
            # 等于目标值
            if tge == 0:
                ret.add(tuple(sorted(data)))
                return
            # 没有符合要求的值
            if tge < 0:
                return

            # 数组中的值可以重复使用
            for c_ in nums:
                dfs(tge - c_, data + [c_])

        # 以数组中的每个值作为一个数进行 递归
        for c in nums:
            temp = [c]
            dfs(target - c, temp)

        print([list(c) for c in ret])
    except Exception as e:
        break