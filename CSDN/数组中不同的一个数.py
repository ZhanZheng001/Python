'''
题目描述
在一个长度为 n 的数组 nums 里的数组中，数字两两相同，有一个不同，找出数组中不同的这一个数。

示例 1
输入：2 3 1 5 2 5 3
输出：1


'''
# 参考代码
# 方法一：
# 遍历数组，通过哈希表记录数字出现的次数

while 1:
    try:
        nums = list(map(int, input().split()))

        dct = {}
        for c in nums:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1

        for k, v in dct.items():
            if v == 1:
                print(k)
    except Exception as e:
        break

# 方法二：
# 使用 count 获取数字的次数，等于1直接输出；

while 1:
    try:
        nums = list(map(int, input().split()))

        for c in nums:
            if nums.count(c) == 1:
                print(c)
    except Exception as e:
        break