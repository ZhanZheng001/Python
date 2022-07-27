'''
题目描述
连续输入字符串(输出次数为 N,字符串长度小于 100)，请按长度为 8 拆分每个字符串后输出到新的字符串数组，
长度不是 8 整数倍的字符串请在后面补数字 0，空字符串不处理。
首先输入一个整数，为要输入的字符串个数。

示例1
输入
2
abc
123456789

输出
abc00000
12345678
90000000

常见的字符串补充方法：
右侧补0

"123".ljust(8, "0")
1
左侧补0

"123".rjust(8, "0")
"123".zfill(8)
1
2
参考代码

'''
while 1:
    try:
        n = 2#int(input())
        for _ in range(n):
            line = input()
            # 从 0 开始，步长为 8 到 len(line) 结束
            for i in range(0, len(line), 8):
                if len(line[i: i+8]) == 8:
                    print(line[i: i+8])
                elif len(line[i: i+8]) > 0:
                # 右侧补0
                    print(line[i: i+8].ljust(8, "0"))
    except Exception as e:
        break