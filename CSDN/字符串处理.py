'''
题目描述
让我们来玩个字符消除游戏吧,给定一个只包含大写字母的字符串 s，消除过程是如下进行的：

如果 s 包含长度为 2 的由相同字母组成的子串，那么这些子串会被消除，余下的子串拼成新的字符串。
例如”ABCCBCCCAA”中”CC”,”CC”和”AA”会被同时消除，余下”AB”,“C”和”B”拼成新的字符串”ABBC”。
上述消除会反复一轮一轮进行，直到新的字符串不包含相邻的相同字符为止。
例如”ABCCBCCCAA”经过一轮消除得到”ABBC”，再经过一轮消除得到”AC”

输入由大写字母组成的字符串 s，长度不超过 100.

若最后可以把整个字符串全部消除,就输出 Yes,否则输出 No.

示例1
输入：

ABCCBA
1
输出：

Yes
1
示例2
输入：

ABCCBCCCAA
1
输出：

No
1
参考代码
我们定义游标 i=1 , 观察 ABCCBCCCAA 的消除过程：

ABCCBCCCAA, i=1, i[0] 不等于 i[1] i 向右移动 i++;
ABCCBCCCAA, i=2, i[1] 不等于 i[2] i 向右移动 i++;
ABCCBCCCAA, i=3, i[2] 等于 i[3] i 消除 CC i–;
ABBCCCAA, i=2, i[1] 等于 i[2] i 消除 BB i–;
ACCCAA, i=1, i[0] 不等于 i[1] i 向右移动 i++;
ACAA, i=2, i[1] 不等于 i[2] i 向右移动 i++;
ACAA, i=3, i[2] 等于 i[3] i 消除 AA i–;
AC, i=2，i 不小于 字符串长度 退出循环；
当 游标 大于剩余字符串长度时退出循环，此时剩下的是不能在消除的字符串；
当 s 为空时 说明字符串全部都消除完了，也需要退出循环；

'''
while 1:
    try:
        s = input()
        i = 1
        while i < len(s):
            if s[i - 1] == s[i]:
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1
        if s:
            print("No")
        else:
            print("yes")
    except Exception as e:
        break