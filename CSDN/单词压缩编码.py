'''
题目描述
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是[“time”,“me”,“bell”]，我们就可以将其表示为 S="time#bell#"和indexes=[0,2,5]。

对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到"#"结束，来恢复我们之前的单词列表。

那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

输入描述：
输入:words=[“time”,“me”,“bell”]
输出:10
说明:S=“time#bell#”， indexes=[0,2,5]。
输出描述：
编码长度

示例 1
输入： time,me,bell
输出： 10

解释：一组有效编码为 s = “time#bell#” 和 indices = [0, 2, 5] 。
words[0] = “time” ，s 开始于 indices[0] = 0 到下一个 ‘#’ 结束的子字符串，如加粗部分所示 “time#bell#”
words[1] = “me” ，s 开始于 indices[1] = 2 到下一个 ‘#’ 结束的子字符串，如加粗部分所示 “time#bell#”
words[2] = “bell” ，s 开始于 indices[2] = 5 到下一个 ‘#’ 结束的子字符串，如加粗部分所示 “time#bell#”

示例 2
输入： t
输出： 2

解释：一组有效编码为 s = “t#” 和 indices = [0] 。

参考代码

'''
while 1:
    try:
        words = input().split(",")
        words = list(set(words))
        N = len(words)
        # 反转每个单词
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        # 字典序排序
        reversed_words.sort()

        res = 0
        for i in range(N):
            if i + 1 < N and reversed_words[i + 1].startswith(reversed_words[i]):
                # 当前单词是下一个单词的前缀，丢弃
                pass
            else:
                res += len(reversed_words[i]) + 1  # 单词加上一个 '#' 的长度

        print(res)
    except Exception as e:
        break