'''
题目描述
现有一字符串仅由( , ) , { , } , [ , ]六种括号组成。

若字符串满足以下条件之一，则为无效字符串：

任一类型的左右括号数量不相等；
存在未按正确顺序（先左后右）闭合的括号。
输出括号的最大嵌套深度，若字符串无效则输出0.
0<=字符串长度<=100000

输入描述：
一个只包( , ) , { , } , [ , ]的字符串。

输出描述:
一个整数，最大括号深度

示例 1
输入:
[]

输出:
1
'''
while 1:
    try:
        nums = input()
        max_ = 0
        stack = []
        for c in nums:
            if c in "{[(":
                stack.append(c)
            else:
                if not stack:
                    print(0)
                    break
                max_ = max(max_, len(stack))
                cr = stack.pop()
                if f"{cr}{c}" not in ["{}", "[]", "()"]:
                    print(0)
                    break
        else:
            print(max_)
    except Exception as e:
        break
