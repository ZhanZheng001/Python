'''
题目描述
已知火星人使用的运算符为#、$，

其与地球人的等价公式如下：

x#y = 2x+3y+4
x$y = 3*x+y+2

其中x、y是无符号整数

地球人公式按C语言规则计算，火星人公式中，$的优先级高于#，相同的运算符，按从左到右的顺序计算 现有一段火星人的字符串报文，请你来翻译并计算结果。

输入描述：

火星人字符串表达式（结尾不带回车换行）

输入的字符串说明：

字符串为仅由无符号整数和操作符（#、$）

组成的计算表达式。例如：123#45#6778

用例保证字符串中，操作数与操作符之间没有任何分隔符。
用例保证操作数取值范围为32位无符号整数。
保证输入以及计算结果不会出现整型溢出。
保证输入的字符串为合法的求值报文，例如：123#45#6778
保证不会出现非法的求值报文，例如类似这样字符串：
#4$5 //缺少操作数
4$5# //缺少操作数
4#$5 //缺少操作数
4 $5 //有空格
3+4-5*6/7 //有其它操作符
12345678987654321$54321 //32位整数计算溢出

输出描述：

根据输入的火星人字符串输出计算结果（结尾不带回车换行）

示例 1
输入：
7#6$5#12

输出：
226

说明：
7#6$5#12
=7#(36+5+2)#12
=7#25#12
=(27+325+4)#12
=93#12
=293+3*12+4
=226
'''

while 1:
    try:
        nums = input()
        # 无符号数
        index_list = [i for i, c in enumerate(nums) if c in "#$"]

        # 按操作符 分隔字符串
        stack = []
        s = 0
        for e in index_list:
            stack.append(int(nums[s:e]))
            stack.append(nums[e])
            s = e + 1
        else:
            stack.append(int(nums[s:]))

        # 计算 优先级高的$ f"3*{x}+{y}+2")
        r_stack = []
        while stack:
            item = stack.pop()
            if item == "$":
                x = stack.pop()
                y = r_stack.pop()
                stack.append(eval(f"3*{x}+{y}+2"))
            else:
                r_stack.append(item)
        stack += r_stack[::-1]

        # 计算 2*{x}+3*{y}+4"
        x = stack[0]
        for i in range(2, len(stack), 2):
            y = stack[i]
            x = eval(f"2*{x}+3*{y}+4")
        print(x)
    except Exception as e:
        break
