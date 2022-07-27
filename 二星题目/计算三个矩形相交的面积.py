'''
题目描述
给出3组点坐标(x, y, w, h)，-1000<x,y<1000，w,h为正整数。
(x, y, w, h)表示平面直角坐标系中的一个矩形：
x, y为矩形左上角坐标点，w, h向右w，向下h。
(x, y, w, h)表示x轴(x, x+w)和y轴(y, y-h)围成的矩形区域；
(0, 0, 2, 2)表示 x轴(0, 2)和y 轴(0, -2)围成的矩形区域；
(3, 5, 4, 6)表示x轴(3, 7)和y轴(5, -1)围成的矩形区域；
求3组坐标构成的矩形区域重合部分的面积。

输入描述：
3行输入分别为3个矩形的位置，分别代表“左上角x坐标”，“左上角y坐标”，“矩形宽”，“矩形高” -1000 <= x,y < 1000

输出描述：
输出3个矩形相交的面积，不相交的输出0。

示例 1
输入：
1 6 4 4
3 5 3 4
0 3 7 3
输出：
2
说明:
给定3个矩形A，B，C
A:左上角坐标(1,6)，宽4、高4B:左上角坐标(3,5)，宽3，高4c:左上角坐标(0,3)，宽7，高33个矩形的相交面积为2，如图所示:
'''
# 根据输入确定矩形的左上角坐标和右下角坐标
# 根据最值生成画布（二位数组）
# 在二维数据上绘制矩形区域
# 三个矩形相交区域数值为3
"""
最终dp的值
dp = [[1, 1, 1, 0, 0, 0],
      [1, 1, 2, 1, 1, 1],
      [1, 1, 2, 1, 1, 1],
      [1, 2, 3, 2, 2, 1],
      [1, 2, 3, 2, 2, 1],
      [1, 2, 2, 1, 1, 0],
      [1, 1, 1, 0, 0, 0]
      ]
"""
while 1:
    try:
        # xs = [] #记录x轴坐标
        # ys = [] #记录y轴坐标
        # nums = [] #记录矩形左上角和右下角x,y轴坐标
        # for _ in range(3):
        #     x1, y1, w, h = list(map(int, input().split())) # x1, y1 左上角
        #     x2, y2 = x1 + w, y1 - h # x2, y2 右下角
        #     xs += [x1, x2]
        #     ys += [y1, y2]
        #     nums.append((x1, y1, x2, y2))
        xs = [1, 5, 3, 6, 0, 7]
        ys = [6, 2, 5, 1, 3, 0]
        nums = [(1, 6, 5, 2), (3, 5, 6, 1), (0, 3, 7, 0)]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        x = 0 - min_x
        y = 0 - min_y # 坐标轴偏移量
        dp = [[0] * abs(max_y-min_y) for _ in range(abs(max_x-min_x))] # 构建二维数据
        for x1, y1, x2, y2 in nums:
            for i in range(min((x2, x1)) + x, max((x2, x1)) + x): # 需要 转成 二维数组的下标
                for j in range(min((y2, y1)) + y, max((y2, y1)) + y):
                    dp[i][j] += 1 # 绘制矩形
        ret = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] == 3:
                    ret += 1
        print(ret)
        break
    except Exception as e:
        break
