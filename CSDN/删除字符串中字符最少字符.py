'''
题目描述
删除字符串中出现次数最少的字符，如果有多个字符出现次数一样，则都删除。

输入描述：
输入 abcdd
字符串中只包含小写英文字母。
输出描述：
dd

示例 1
输入：

abcdd
1
输出：

dd
1
解释：
a 出现1次
b 出现1次
c 出现1次
d 出现2次
删除 abc

示例 2
输入：

abcdddeddccfhb
1
输出：

bcdddddccb
1

'''
# 参考代码
# 首先遍历字符串，使用哈希表记录存储 字符 和字符出现的次数，找到出现最少的字符们，在原字符串上移除这些字符。

while 1:
    try:
        nums = input()

        dct = {}
        for c in nums:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1

        min_ = min(dct.values())
        for k, v in dct.items():
            if v == min_:
                nums = nums.replace(k, "")

        print(nums)

    except Exception as e:
        break