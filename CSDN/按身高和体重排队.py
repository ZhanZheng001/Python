'''
题目描述
某学校举行运动会，学生们按编号(1、 2、 3…n)进行标识，现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列；对于身高体重都相同的人，维持原有的编号顺序关系。请输出排列后的学生编号。
输入描述：
两个序列，每个序列由 n 个正整数组成（0<n<=100）。第一个序列中的数值代表身高，第二个序列中的数值代表体重。
输出描述：
排列结果，每个数值都是原始序列中的学生编号，编号从 1 开始。

示例 1
输入：

4
100 100 120 130
40 30 60 50
1
2
3
输出：

2 1 3 4
1
sorted 语法：
sorted(iterable, key=None, reverse=False)

参数说明：
iterable – 可迭代对象。
key – 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse – 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
返回值
返回重新排序的列表。

多条件排序
当需要进行多条件排序时多可以使用 sorted 方法实现，按照需要的 排序规则定义 key=lambda ；

类似的题目还有 【华为机试真题 Python实现】奥运会奖牌榜的排名
根据 金牌数、银牌数、铜牌数、国家首字母 四个条件排序。

如果排序时 两个条件的排序 方向不同时，可以在逆序的条件前添加负号，例如：key=lambda x: (x[1], -x[2])

参考代码

'''
while 1:
    try:
        lens = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        nums = []
        for i in range(1, lens+1):
            nums.append((i, a[i-1], b[i-1]))

        nums = sorted(nums, key=lambda x: (x[1], x[2]))
        print(" ".join([str(i[0]) for i in nums]))
    except Exception as e:
        break