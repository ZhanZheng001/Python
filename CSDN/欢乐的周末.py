'''
题目描述
小华和小为是很要好的朋友，他们约定周末一起吃饭通过手机交流，他们在地图上选择了多个聚餐地点（由于自然地形等原因，部分聚餐地点不可达），求小华和小为都能到达的聚餐地点有多少个？

输入描述：
第一行输入m和n，m代表地图的长度，n代表地图的宽度。
第二行开始具体输入地图信息，地图信息包含：
0 为通畅的道路
1 为障碍物（旦仅1为障碍物）
2 为小华或者小为，地图中必定有且仅有2个（非障碍物)
3 为被选中的聚餐地点（非障碍物）

输出描述：
可以被两方都到达的聚餐地点数量，行末无空格。

示例 1
输入：
4 4
2 1 0 3
0 1 2 1
0 3 0 0
0 0 0 0

输出：
2

说明：
第一行输入地图的长宽为3和4。
第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个)；
代表可以通行的位置；1代表不可以通行的位置。
此时两者能都能到达的聚餐位置有2处。

示例 2
输入：
4 4
2 1 2 3
0 1 0 0
0 1 0 0
0 1 0 0

输出：
0

说明：
第一行输入地图的长宽为4和4。
第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个）
代表可以通行的位置；1代表不可以通行的位置。
由于图中小华和小为之问有个阻隔，此时，没有两人都能到达的聚餐地址，故而返回0。

参考代码
首先我们需要遍历输入项，
构建二维数组；
找到起始点（也就是小为，小华的坐标）；
找到终止点（聚餐地点坐标）；
循环聚餐地点，看从小为，小华坐标出发能否都能到达；
'''
while 1:
    try:
        n, m = map(int, input().split())

        map_ = [input().split() for i in range(m)]
        # 小华小为的坐标
        start_spots = []
        # 聚餐点坐标
        end_spots = []

        for i in range(m):
            for j in range(n):
                if map_[i][j] == "2":
                    start_spots.append((i, j))
                elif map_[i][j] == "3":
                    end_spots.append((i, j))

        count = 0
        for end_ in end_spots:

            def dfs(si, sj, cache):
                if (si, sj) in cache:
                    return False
                cache.append((si, sj))
                # 控制地图边界
                if not (0 <= si < m and 0 <= sj < n):
                    return False
                # 遇到障碍物
                if map_[si][sj] == "1":
                    return False
                if (si, sj) == tuple(end_):
                    return True

                # 有四种情况可以向上下左右走
                return dfs(si+1, sj, cache) or dfs(si-1, sj, cache) \
                       or dfs(si, sj+1, cache) or dfs(si, sj-1, cache)

            # 已到达的坐标，避免重复计算
            cache_a = []
            cache_b = []
            if dfs(start_spots[0][0], start_spots[0][1], cache_a) \
                    and dfs(start_spots[1][0], start_spots[1][1], cache_b):
                count += 1

        print(count)
    except Exception as e:
        break
