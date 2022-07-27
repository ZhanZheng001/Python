'''
题目描述
编程的时候， if 条件里面的“(”、 “)”括号经常出现不匹配的情况导致编译不过，请编写程序检测输入一行 if 语句中的圆括号是否匹配正确。

同时输出语句中出现的左括号和右括号数量，如 if((a==1)&&(b==1))是正确的，而if((a==1))&&(b==1)) 是错误的。

注意 if 语句的最外面至少有一对括号。

提示：用堆栈来做。

示例 1
输入： if((a==1)&&(b==1))
输出： RIGTH 3 3

示例 2
输入： if((a==1))&&(b==1))
输出： WRONG 3 4

参考代码

'''
while 1:
    try:
        nums = input()

        flg = "RIGTH"
        stack = []
        for c in nums:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack or stack.pop() != "(":
                    flg = "WRONG"
                    break
        if stack:
            flg = "WRONG"

        print(f"{flg} {nums.count('(')} {nums.count(')')}")
    except Exception as e:
        break