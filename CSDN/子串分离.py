'''
题目描述
通过键盘输入任意一个字符串序列，字符串可能包含多个子串，子串以空格分隔。
请编写一个程序，自动分离出各个子串，并使用’,’将其分隔，并且在最后也补充一个’,’并将子串存储。
如果输入“abc def gh i d”，结果将是 abc,def,gh,i,d,

示例 1
输入：abc def gh i d
输出：abc,def,gh,i,d,

参考代码

'''
while 1:
    try:
        nums = input()

        print(f'{nums.replace(" ", ",")},')
    except Exception as e:
        break