'''
题目描述
完成从一个正整数到 Excel 编号之间的转换。

用过 excel 的都知道 excel 的列编号是这样的：
abc…zaaabac…azbabbbc…yzzazbzc…zzaaaaabaac…

分别代表以下编号：
123…26272829…52535455…676677678679…702703704705…请写个函数，完成从一个正整数到这种字符串之间的转换。

功能正整数到 Excel 编号字符串转换。

示例 1：
输入：1
输出：A

示例 2：
输入：28
输出：AB

示例 3：
输入：701
输出：ZY

示例 4：
输入：2147483647
输出：FXSHRXW

参考代码
我的第一感觉是 A,B,C…,Z,AA,AB,AC,…ZZ,AAA,AAB…可以转换成“进制数”表示形式，由于一共 26 个英文字母，可以转换成 26 进制表示形式。转换成 26 进制形式后 26 进制
数 1 对应 A、 2 对应 B…25 对应 Y，这样 Z 只能对应 26 进制数 10。而十进制数 27 转换成 26 进制数为 11 即可对应成 AA，十进制数 52 转换成 26 进制数为 20 对应为 AZ。所有
我们需要对能被 26 整除的正整数进行特殊处理。


'''
while 1:
    try:
        columnNumber = int(input())
        base = ord("A")
        dp = []

        tep = 26
        while tep < columnNumber:
            num = columnNumber % tep
            if num == 0:
                dp.append(tep)
                columnNumber = columnNumber // tep - 1
            else:
                dp.append(num)
                columnNumber = columnNumber // tep
        else:
            dp.append(columnNumber)
        print("".join([chr(base + c - 1) for c in dp[::-1]]))
    except Exception as e:
        break