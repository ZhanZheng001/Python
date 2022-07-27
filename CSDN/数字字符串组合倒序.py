'''
题目描述
对数字，字符，数字串，字符串，以及数字与字符串组合进行倒序排列。

字符范围：由 a 到 z， A 到 Z，数字范围：由 0 到 9符号”的定义：
（1）”做为连接符使用时作为字符串的一部分，例如“20-years”作为一个整体字符串呈现；
（2）连续出现 2 个’及以上时视为字符串间隔符，如“out–standing"中的“-“视为间隔符，是 2 个独立整体字符串"out"和"standing"；

除了 1， 2 里面定义的字符以外其他的所有字符，都是非法字符，作为字符串的间隔符处理，倒序后间隔符作为空格处理；

要求倒排后的单词间隔符以一个空格表示；如果有多个间隔符时，倒排转换后也只介许出现一个字格间隔符：

示例1
输入：

I am an 20-years out--standing @ * -stu- dent
1
输出：

dent stu standing out 20-years an am I
1

'''
# 参考代码
def fun(st, dp):
    if st:
        if "--" in st:
            dp += st.split("--")
        elif st[-1] == "-":
            dp.append(st[:-1])
        else:
            dp.append(st)

while 1:
    try:
        dp = []
        temp = ""
        for c in input():
            if ("A" <= c <= "Z"
                    or "a" <= c <= "z"
                    or "0" <= c <= "9"
                    or (c == "-" and temp)):
                temp += c
            else:
                fun(temp, dp)
                temp = ""

        fun(temp, dp)

        print(" ".join(dp[::-1]))
    except Exception as e:
        break