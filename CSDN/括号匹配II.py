'''
题目描述
给定一个字符串，里边可能包含“()”、“[]”、“{}”三种括号，请编写程序检查该字符串中的括号是否成对出现，且嵌套关系正确。

输出：
true:若括号成对出现且嵌套关系正确，或该字符串中无括号字符；
false:若未正确使用括号字符。

实现时，无需考虑非法输入。

输入描述：
输入为：
字符串
例子： (1+2)/(0.5+1)

输出描述：
输出为：
字符串
例子： true

示例 1
输入：(1+2)/(0.5+1)
输出：true

参考代码

'''
while 1:
    try:
        nums = input()

        stack = []
        flg = True
        for c in nums:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if stack:
                    w = stack.pop()
                    if not ((c == ")" and w == "(")
                            or (c == "]" and w == "[")
                            or (c == "}" and w == "{")):
                        flg = False
                        break
                else:
                    flg = False
                    break
        if stack:
            flg = False

        print("true" if flg else "false")
    except Exception as e:
        break