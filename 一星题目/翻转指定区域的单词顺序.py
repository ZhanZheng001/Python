'''
输入一个英文文章片段,翻转指定区域的单词顺序,标点符号和普通字母一样处理
例如输入字符串 I am a developer.
[0,3]
则输出 developer. a am I

输入描述
 使用换行隔开3个参数
 第一个参数为文章内容 即英文字符串
 第二个参数为翻转起始单词下标，下标从0开始
 第三个参数为结束单词下标
输出描述
 翻转后英文文章片段每个单词之间以一个半角空格分割输出

例子1:
输入
   I am a developer.
   1
   2
输出
   I a am developer.
例子2:
输入
  hello world!
  0
  3
  输出
  world! hello
输入字符串可以在前面或者后面包含多个空格,但是翻转后的字符不能包括
指定反转区间只有一个单词或无有效单词,则输出EMPTY
'''
while True:
    try:
        list1 = "I am a developer.".strip().split(" ")
        m,n = int("0"),int("3")
        list1[m:n+1] = list1[m:n+1][::-1]
        print(" ".join(list1))
        break
    except:
        break
