'''
题目描述
游戏规则：输入一个只包含英文字母的字符串，字符串中的两个字母如果相邻且相同，就可以消除。

在字符串上反复执行消除的动作，直到无法继续消除为止，此时游戏结束。

输出最终得到的字符串长度。

示例 1
输入：
aaaaaaa

输出：
1

示例 2
输入：
abcaacba

输出：
0
'''
while 1:
    try:
        nums = input()
        i = 0
        while i < len(nums):
            if nums[i] * 2 in nums:
                nums = nums.replace(nums[i] * 2, "")
                i = max(0, i-1)
            else:
                i += 1
        print(len(nums))
    except Exception as e:
        break
