'''
题目描述
每个句子由多个单词组成，句子中的每个单词的长度都可能不一样， 我们假设每个单词的长度 LW 为该单词的重量，请给出整个句子的平均重量 V。
输入描述：
输入只有一行，包含一个字符串 S(长度不会超过 100)，代表整个句子，句子中只包含大小写的英文字母（不包含标点符号），每个单词之间有一个空格。
**输出描述： **
输出 S 的平均重量 V（每个单词的长度之和/单词个数） (四舍五入保留两位小数)。
示例 1
输入：
Who Love Mate
1
输出：
3.67
1
参考代码
Python实现：


'''
while 1:
    try:
        nums = input().split()
        print(round(sum([len(i) for i in nums])/len(nums), 2))
    except Exception as e:
        break