'''
题目描述
给一个数组对元素分组，要求只有满足 1、每组里的数据都相等； 2、每组的元素个数都是 N（N>=2），满足两个条件才允许分组，返回从小到大的分组。

示例 1
输入：1,2,2,1
输出：
1,1
2,2

示例 2
输入：1,1,4,3,3
输出：
-1

参考代码

'''
while 1:
    try:
        nums = list(map(int, input().split(",")))

        dct = {}
        for c in nums:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1
        if len(set(dct.values())) == 1:
            count = max(dct.values())
            keys = sorted(dct.keys())

            for i in keys:
                print(",".join([str(i)]*count))
        else:
            print(-1)

    except Exception as e:
        break