'''
题目描述
一组工人搬运一批水果，用一维数组存储工人编号和水果名称以及搬运重量，要求先按水果分组，然后按搬运重量排序输出。

输入描述：
接下来的 N 行每行包括两个整数 p 和 q,分别代表每个工人的编号和搬运重量，以及一个字符串 m,代表水果的名称。

输出描述：
先按水果分组，然后按工人的搬运重量从小到大进行排序，并将排序后的信息打印出来。如果工人搬运的重量相同，则按照编号的大小从小到大排序，并且要求水果的输
出次序同输入次序。

示例 1
输入：

5
Apple 1 80
Apple 2 62
Apple 4 73
Orange 4 65
Orange 1 90
Apple 3 91
Orange 3 88
Orange 5 90
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

Apple 2 62
Apple 4 73
Apple 1 80
Apple 3 91
Orange 4 65
Orange 3 88
Orange 1 90
Orange 5 90
1
2
3
4
5
6
7
8
参考代码


'''
while 1:
    try:
        _ = input()
        nums = []
        while 1:
            try:
                m, p, q = input().split()
                nums.append((m, int(p), int(q)))
            except:
                break

        nums = sorted(nums, key=lambda x: (x[0], x[2], x[1]))
        for i in nums:
            print(" ".join(list(map(str, i))))
    except Exception as e:
        break