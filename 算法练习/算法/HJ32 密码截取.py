'''
描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，
但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,
123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

本题含有多组样例输入。

输入描述：
输入一个字符串

输出描述：
返回有效密码串的最大长度

示例1
输入：
ABBA
复制
输出：
4
'''
while True:
    try:
        passwd = input()
        num = 0
        for i in range(len(passwd) - 1):
            if passwd[i] == passwd[i + 1]:
                first = i
                last = i + 1
                while first >= 0 and last < len(passwd) and passwd[first] == passwd[last]:
                    first -= 1
                    last += 1
                num = max(num, last - first - 1)

            elif passwd[i - 1] == passwd[i + 1]:
                first = i - 1
                last = i + 1
                while first >= 0 and last < len(passwd) and passwd[first] == passwd[last]:
                    first -= 1
                    last += 1
                num = max(num, last - first - 1)
        print(num)
    except:
        break