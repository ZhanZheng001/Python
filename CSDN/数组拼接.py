'''
题目描述
现在有多组整数数组,需要将他们合并成一个新的数组,合并规则,从每个数组里按顺序取出国定长度的内容合并到新的数组中,取完的内容会删除掉,如果该行不足固定长度或者
已经为空,则直接取出剩余部分的内容放到新的数姐中,继续下一行。

输入描述：
第一行是每次读取的固定长度,长度>0
第 2-n 行是需要合井的数姐,不同的数组用回车换行分隔,数组内部用逗号分隔

输出描述：
输出一个新的数组，用逗号分隔。

示例 1
输入：
3
2,5,6,7,9,5,7
1,7,4,3,4
输出：
2,5,6,1,7,4,7,9,5,3,4,7

如样例 1，
获得长度 3,遍历第一行,获得 2， 5， 6；
再遍历第二行,获得 1， 7， 4；
再循环回到第一行,获得 7， 9， 5；
再遍历第二行,获得 3， 4；
再回到第一行,获得 7,按顺序拼接成最终结果。

参考代码

'''
while 1:
    try:
        n = int(input())

        nums = [input().split(',') for _ in range(n-1)]

        dp = []
        i = 0
        while nums:
            if len(nums[i]) > n:
                temp = nums[i][:n]
                nums[i] = nums[i][n:]
            else:
                temp = nums[i]
                nums.pop(i)
            dp += temp
            i += 1

            if i >= len(nums):
                i = 0

        print(",".join(dp))
    except Exception as e:
        break