'''
题目描述
输入一个由随机数组成的数列（数列中每个数均是大于 0 的整数，长度已知）， 和初始计数值 m。从数列首位置开始计数，计数到 m 后，将数列该位置数值替换计数值 m，并将数列该位置数值出列，然后从下一位置从新开始计数，直到数列所有数值出列为止。
如果计数到达数列尾段，则返回数列首位置继续计数。
请编程实现上述计数过程，同时输出数值出列的顺序

比如：
输入的随机数列为： 3,1,2,4，初始计数值 m=7，从数列首位置开始计数（数值 3 所在位置）
第一轮计数出列数字为 2，计数值更新 m=2，出列后数列为 3,1,4，从数值 4 所在位置从新开始计数
第二轮计数出列数字为 3，计数值更新 m=3，出列后数列为 1,4，从数值 1 所在位置开始计数
第三轮计数出列数字为 1，计数值更新 m=1，出列后数列为 4，从数值 4 所在位置开始计数
最后一轮计数出列数字为 4，计数过程完成。输出数值出列顺序为： 2,3,1,4。

示例 1
输入：
3,1,2,4
7
输出：
2,3,1,4

参考代码

'''
while 1:
    try:
        nums = list(map(int, input().split(",")))
        m = int(input())

        dp = []
        i = 0
        c = 1
        while nums:
            if i == len(nums):
                i = 0

            if c % m == 0:
                m = nums.pop(i)
                dp.append(m)
                c = 1
            else:
                i += 1
                c += 1

        print(",".join(map(str, dp)))
    except Exception as e:
        break