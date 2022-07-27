'''
题目描述
开头和结尾都是元音字母（aeiouAEIOU）的字符串为元音字符串，其中混杂的非元音字母数量为其瑕疵度。

比如:
“a” 、 “aa”是元音字符串，其瑕疵度都为0
“aiur”不是元音字符串（结尾不是元音字符）
“abira”是元音字符串，其瑕疵度为2

给定一个字符串，请找出指定瑕疵度的最长元音字符子串，并输出其长度，如果找不到满足条件的元音字符子串，输出0。

输入描述：
首行输入是一个整数，表示预期的瑕疵度flaw，取值范围[0, 65535]。
接下来一行是一个仅由字符a-z和A-Z组成的字符串，字符串长度(0, 65535]。

输出描述：
输出为一个整数，代表满足条件的元音字符子串的长度。

示例 1
输入：
0
asdbuiodevauufgh

输出：
3
'''
bct = "aeiou"

while 1:
    try:
        k = int(input())
        nums = input()

        n = len(nums)
        nums = [1 if c in bct else 0 for c in nums]
        print(nums)
        max_ = 0
        i = 0
        j = min(k, n)
        while j < len(nums):
            count = nums[i:j].count(0)
            if count < k:
                j += 1
            elif count == k:
                max_ = max([j-i, max_])
                j += 1
            else:
                i += 1
        else:
            max_ = max([j - i, max_])

        print(max_)
    except Exception as e:
        break
