'''
描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。s
输入n，请输出n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
本题输入含有多组样例。

输入描述：
输入一个数字n

输出描述：
输出不超过n的完全数的个数

示例1
输入：
1000
7
100
复制
输出：
3
1
2

'''

while True:
    try:
        a = int(input())
        res =[]
        for i in range(2,a+1):
            sum=1
            for j in range(2,i//2+1):
                if i%j == 0:
                    sum += j
            if i == sum:
                res.append(sum)
        print(res)
        print(len(res))
#内存超过32M,通过上面的计算，可以得到
#         a=int(input())
#         print(len(list(filter(lambda x:x<=a, [6,28,496,8128]))))
    except:
        break









