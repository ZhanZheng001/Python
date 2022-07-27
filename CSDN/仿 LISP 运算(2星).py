'''
题目描述
LISP 语言唯一的语法就是括号要配对。 形如 (OP P1 P2 …)，括号内元素由单个空格分割。
其中第一个元素 OP 为操作符，后续元素均为其参数，参数个数取决于操作符类型
注意：参数 P1, P2 也有可能是另外一个嵌套的 (OP P1 P2 …) 当前 OP 类型为 add / sub / mul / div（全小写），分别代表整数的加减乘除法 简单起见，所有 OP 参数个数均为 2

举例:
输入： (mul 3 -7)
输出： -21

输入： (add 1 2)
输出： 3

输入： (sub (mul 2 4) (div 9 3))
输出： 5

输入： (div 1 0)
输出： error

题目涉及数字均为整数，可能为负；不考虑 32 位溢出翻转，计算过程中也不会发生 32 位溢出翻转 除零错误时，输出 “error”，除法遇除不尽，向下取整，即 3/2 = 1

输入描述：
输入为长度不超过 512 的字符串，用例保证了无语法错误

输出描述：
输出计算结果或者“error”

示例 1
输入： (div 12 (sub 45 45))

输出：error

示例 1
输入：
输出：

参考代码

'''
while 1:
    try:
        nums = input().split()
        stack_a = []
        stack_b = []

        for c in nums:
            if "(" in c:
                stack_a.append("(")
                stack_a.append(c[1:])
            elif ")" in c:
                stack_a.append(c[:c.index(")")])
                stack_a += list(c[c.index(")"):])
            else:
                stack_a.append(c)

        while stack_a:
            temp = stack_a.pop()
            if temp == ")":
                stack_b.append(temp)
            elif temp == "(":
                com = stack_b.pop()
                # add / sub / mul / div
                a = int(stack_b.pop())
                b = int(stack_b.pop())
                # 当前计算公式的右括号
                stack_b.pop()
                if com == "add":
                    stack_b.append(a+b)
                elif com == "sub":
                    stack_b.append(a-b)
                elif com == "mul":
                    stack_b.append(a*b)
                else:
                    if b == 0:
                        print("error")
                        break
                    stack_b.append(a//b)
            else:
                stack_b.append(temp)

        if stack_b:
            print(stack_b.pop())
    except Exception as e:
        break