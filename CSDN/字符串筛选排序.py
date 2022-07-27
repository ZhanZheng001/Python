'''
题目描述
输入一个由 n 个大小写字母组成的字符串，按照 Ascii 码值从小到大的排序规则，查找字符串中第 k 个最小 ascii 码值的字母（k>=1），输出该字母所在字符串的位
置索引(字符串的第一个字符位置索引为 0）。

k 如果大于字符串长度，则输出最大 ascii 值的字母所在字符串的位置索引，如果有重复的字母，则输出字母的最小位置索引。

输入描述：
第一行输入一个由大小写字母组成的字符串
第二行输入 k， k 必须大于 0， k 可以大于输入字符串的长度
输出描述：
输出字符串中第 k 个最小 ascii 码值的字母所在字符串的位置索引。 k 如果大于字符串长度，则输出最大 ascii 值的字母所在字符串的位置索引，如果第 k 个最小 ascii 码
值的字母存在重复，则输出该字母的最小位置索引。

示例 1
输入：

AbCdeFG
3
1
2
输出：

5
1
示例 2
输入：

AbCdeFeeeeG
20
1
2
输出：

4
1
参考代码
以 AbCdeFG 为例；
首先需要对输入的字符串排序，原始字符串需要确定输出的字符，将排序后的字符串存储在新的对象中，排序后 nums = ['A', 'C', 'F', 'G', 'b', 'd', 'e']；
找到第 k 个最小的字符 nums[k-1] 即：F；
在原始字符串中确认 F 的位置 5 并输出。


'''
while 1:
    try:

        nums = input()
        k = int(input())
        nums_std = sorted(nums)
        if k > len(nums):
            flg = nums_std[-1]
        else:
            flg = nums_std[k-1]

        print(nums.index(flg))
    except Exception as e:
        break