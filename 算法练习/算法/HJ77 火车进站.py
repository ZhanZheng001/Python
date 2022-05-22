'''
描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
要求输出所有火车出站的方案，以字典序排序输出。
输入描述：
有多组测试用例，每一组第一行输入一个正整数N（0

输出描述：
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入：
3
1 2 3
复制
输出：
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
复制
说明：
第一种方案：1进、1出、2进、2出、3进、3出
第二种方案：1进、1出、2进、3进、3出、2出
第三种方案：1进、2进、2出、1出、3进、3出
第四种方案：1进、2进、2出、3进、3出、1出
第五种方案：1进、2进、3进、3出、2出、1出
请注意，[3,1,2]这个序列是不可能实现的。
'''
def rec_trains(cur_idx, in_trains, out_trains):
    if trains[-1] in in_trains:
        res.append(' '.join(out_trains + in_trains[::-1]))#最后一个车出站，即输出一种方案
        return
    elif in_trains == []:
        rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)#0号车进站
    else:
        rec_trains(cur_idx, in_trains[:-1], out_trains + [in_trains[-1]])#如果出站
        rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)#如果进站
while True:
    try:
        # n = int(input())
        n = 3
        # trains = input().strip().split(' ')
        trains = ['1', '2', '3']
        res = []
        rec_trains(0, [], [])#初始情况下，待入站序号cur_idx为0号车，in_trains已进站列表为空，out_trains已出站列表为空
        res.sort()
        print('\n'.join(res))
        break
    except:
        break