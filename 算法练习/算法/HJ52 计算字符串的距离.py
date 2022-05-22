'''
描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。

Ex：
字符串A:abcdefg
字符串B: abcdef
通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。
要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
本题含有多组输入数据。
输入描述：
每组用例一共2行，为输入的两个字符串
输出描述：
每组用例输出一行，代表字符串的距离
示例1
输入：
abcdefg
abcdef
abcde
abcdf
abcde
bcdef
复制
输出：
1
1
2
'''
while 1:
    try:
        # s1 = '#'+input()
        # s2 = '#'+input()
        s1 = '#abc'
        s2 = '#ab'
        m1, m2 = len(s1), len(s2)
        print('m1=',m1,'m2=',m2)
        # 用一个占位符表示字符串的开头
        l = [[0 for i in range(m1)] for j in range(m2)]
        for i in range(m2):
            l[i][0] = i
        for j in range(m1):
            l[0][j] = j
        print(l)
        for i in range(1,m2):
            for j in range(1,m1):
                # [i,j]处来自于[i-1,j] [i,j-1] [i-1,j-1]这三个方向走来，
                # l[i-1,j]+1 和l[i,j-1]+1对应着增删，l[i-1][j-1]对应着改，当s1[i]==s2[j]时不用改，否则改
                left = l[i-1][j]+1
                down = l[i][j-1]+1
                left_down = l[i-1][j-1]
                print(left,down,left_down)
                # 当两个点不相同时，左上方加一，否则不用修改
                if s1[j] != s2[i]:
                        left_down += 1
                l[i][j] = min(left, down, left_down)
                print(f'+++++l[{i}][{j}]+++++++',l)
        print(l[-1][-1])
        break
    except:
        break
