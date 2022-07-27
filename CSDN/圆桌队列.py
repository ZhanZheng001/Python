'''
题目描述
一组人（n 个），围成一圈，从某人开始数到第三个的人出列，再接着从下一个人开始数，最终输出最终出列的人。

约瑟夫环是一个数学的应用问题：已知 n 个人（以编号 1，2， 3…n 分别表示） 围坐在一张圆桌周围。从编号为 k 的人开始报数，数到 m 的那个人出列；他的下一个人又从 1 开始报数，数到 m 的那个人又出列；依此规律重复下去，直到圆桌周围的人全部出列。

示例 1
输入：

10
3
3
1
2
3
输出：

7
1
参考代码

'''
while 1:
    try:
        n = int(input())
        k = int(input())
        m = int(input())

        nums = list(range(1, n+1))
        nums = nums[k-1:] + nums[:k-1]
        dp = []

        while len(nums) >= m:
            cache = list(range(m - 1, len(nums), m))
            nums_ = []
            for i in range(len(nums)):
                if i in cache:
                    dp.append(nums[i])
                elif i > cache[-1]:
                    nums = nums[i:] + nums_
                    break
                else:
                    nums_.append(nums[i])
            else:
                nums = nums_

        print(dp[-1])
    except Exception as e:
        break