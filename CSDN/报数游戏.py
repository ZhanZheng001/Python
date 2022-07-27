'''
题目描述
100个人围成一圈，每个人有一个编码，编号从1开始到100。他们从1开始依次报数，报到为M的人自动退出圈圈，然后下一个人接着从1开始报数，直到剩余的人数小于M。请问最后剩余的人在原先的编号为多少？

输入描述：
输入一个整数参数M

输出描述：
如果输入参数M小于等于1或者大于等于100，输出“ERROR!”；否则按照原先的编号从小到大的顺序，以英文逗号分割输出编号字符串

示例 1
输入：3
输出：58,91

说明:
输入M为3，最后剩下两个人

示例 2
输入：4
输出：34,45,97

说明
输入M为4，最后剩下三个人

参考代码

'''
while 1:
    try:
        m = int(input())

        if 1 >= m or m >= 100:
            print("ERROR!")
        else:
            # 模拟1-100的圈
            nums = list(range(1, 101))
            i = 0
            while len(nums) >= m:
                # 记录需要移除的数，也就是报的 m 的数
                cache = list(range(m - 1, len(nums), m))
                nums_ = []
                for i in range(len(nums)):
                    # 列表最后一个 m 后面的数，再下一轮 是列表的头
                    # 比如 [1,2,3,4,5] 报数到 3 ；
                    # 下一轮是 [4,5,1,2]
                    if i > cache[-1]:
                        nums = nums[i:] + nums_
                        break
                    elif i not in cache:
                        nums_.append(nums[i])
                else:
                    nums = nums_

            nums.sort()
            print(",".join(list(map(str, nums))))
    except Exception as e:
        break
