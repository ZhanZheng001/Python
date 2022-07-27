'''
题目描述
奖牌榜的排名算法要求如下，首先是按照金牌🏅总数排序的，如果是同等金牌的情况下，再根据银牌🥈的总数进行排序，同样在金牌跟银牌数量相等的情况下，在根据铜牌🥉的数量进行排名。在遇到金牌🏅、银牌🥈跟铜牌🥉数量一样的情况下，根据国家的名称首字母序排序。

输入描述：
第一行输入要排序的国家的个数n，之后n行分别输入国家的名字、金牌总数、银牌总数和铜牌总数，以一个空格隔开。

输出描述：
按照降序方式输出国家的名字。

示例1
输入：

8
China 9 4 2
Germany 12 10 5
Norway 16 8 13
Britain 1 1 0
Belgium 1 0 1
Italy 2 7 8
Netherlands 8 5 4
CzechRepublic 1 0 1
1
2
3
4
5
6
7
8
9
输出：

Norway 16 8 13
Germany 12 10 5
China 9 4 2
Netherlands 8 5 4
Italy 2 7 8
Britain 1 1 0
Belgium 1 0 1
CzechRepublic 1 0 1
1
2
3
4
5
6
7
8
分析
就2022年北京冬奥会一共会产生327枚奖牌。其中金牌银牌铜牌各109枚。
使用 sorted 按排序规则生成排序值并格式化输出。

参考代码

'''
while 1:
    try:
        count = int(input())

        temp = {}
        for _ in range(count):
            rst = input().split()
            temp[rst[0]] = (int(rst[1]), int(rst[2]), int(rst[3]), (100 - ord(rst[0][0].upper())))

        dex_lst = sorted(temp.items(), key=lambda itm: itm[1], reverse=True)

        for name in dex_lst:
            print("%s %d %d %d" % (name[0], *name[1][:3]))
    except:
        break