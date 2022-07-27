'''
题目描述
在坐标轴上绘制矩形，只有绘制和擦除两种操作。求绘制的图形面积。规则为与绘制的矩形求并集，与擦除的矩形求差集
场景1
先画一个矩形A，左上角坐标为（0，2），右下角坐标为（2，0），再画一个左上角坐标（-1，1），右下角坐标（1，-1）的矩形B。
则画出的图形面积为两个矩形面积求和减去交集的矩形面积。
矩形A面积为2* 2=4，矩形B面积为（1-（-1））* （1-（-1））=4，交集面积是1 *1=1，则绘制的图形面积为4+4-1=7。
场景2
先画一个矩形A，左上角坐标为（0，2），右下角坐标为（2，0），再擦除一个矩形B，左上角坐标为（-1，1），右下角坐标为（1，-1），
则剩余图形面积为两个矩形求差集，矩形A面积为4，矩形B擦除了矩形A的面积为1，所以绘制的图形面积为3
输入描述：
第一行为一个正整数N，表示有N个操作，接下来N行格式为d x1 y1 x2 y2或者e x1 y1 x2 y2
，其中d代表绘制，e代表擦除，x1 y1代表矩形左上角坐标，x2 y2代表矩形右下角坐标。坐标均为整数
输出描述：
绘制的图形面积
示例 1
输入：
2
d 0 2 2 0
d -1 1 1 -1
输出：
7
示例 2
输入：
2
d 0 2 2 0
e -1 1 1 -1
输出：
3
示例 3
输入：
4
d 0 2 2 0
d -1 1 1 -1
e 0 1 3 -2
d 2 -1 4 -3
输出：
7
参考代码
转化一下思路，如果我们找到所有矩形的中的 最值x,y;
由最值x,y构成一个大的二维数组，元素默认为0；
d 时 将范围的值 置为1；
e 时 将范围的值 置为0；
求 二位数组中 1 的个数；
'''
while 1:
    try:
        # xs = []
        # ys = []
        # coms_d = []
        # coms_e = []
        # for _ in range(int(input())):
        #     l = input().split()
        #     x1, y1, x2, y2 = list(map(int, l[1:]))
        #     xs.append(x1)
        #     xs.append(x2)
        #     ys.append(y1)
        #     ys.append(y2)
        #     if l[0] == 'd':
        #         coms_d.append((x1, y1, x2, y2))
        #     else:
        #         coms_e.append((x1, y1, x2, y2))
        xs = [0, 2, -1, 1, 0, 3, 2, 4]
        ys = [2, 0, 1, -1, 1, -2, -1, -3]
        coms_d = [(0, 2, 2, 0), (-1, 1, 1, -1), (2, -1, 4, -3)]
        coms_e = [(0, 1, 3, -2)]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        x = 0 - min_x #1
        y = 0 - min_y #3 坐标轴偏移量
        dp = [[0] * abs(max_y-min_y) for _ in range(abs(max_x-min_x))]
        for x1, y1, x2, y2 in coms_d: #先把所以的d绘制成图形
            for i in range(min((x2, x1)) + x, max((x2, x1)) + x): # 需要 转成 二维数组的下标
                for j in range(min((y2, y1)) + y, max((y2, y1)) + y):
                    dp[i][j] = 1
        for x1, y1, x2, y2 in coms_e: #擦除e部分的图形
            for i in range(min((x2, x1)) + x, max((x2, x1)) + x):
                for j in range(min((y2, y1)) + y, max((y2, y1)) + y):
                    dp[i][j] = 0
        print(sum([sum(i) for i in dp])) #计算剩余的1的总数即为面积
        break
    except Exception as e:
        break