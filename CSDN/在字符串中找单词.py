'''
题目描述
在给定字符串中找出单词（ “单词”由大写字母和小写字母字符构成，其他非字母字符视为单词的间隔，如空格、问号、数字等等；另外单个字母不算单词）；

找到单词后，按照长度进行降序排序，（排序时如果长度相同，则按出现的顺序进行排列），然后输出到一个新的字符串中；

如果某个单词重复出现多次，则只输出一次；如果整个输入的字符串中没有找到单词，请输出空串。

输出的单词之间使用一个“空格”隔开，最后一个单词后不加空格。

示例 1
输入：Hello, my name is John
输出：Hello name John my is

参考代码

'''
while 1:
    try:
        nums = input()+"#"

        dp = []

        temp = ""
        for c in nums:
            if "a" <= c <= "z" or "A" <= c <= "Z":
                temp += c
            else:
                if len(temp) > 1 and temp not in dp:
                    dp.append(temp)
                temp = ""
        dp = sorted(dp, key=lambda x: len(x), reverse=True)
        print(" ".join(dp))
    except Exception as e:
        break