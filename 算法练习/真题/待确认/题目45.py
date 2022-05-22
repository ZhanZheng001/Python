'''
给定一个正整数数组
检查数组中是否存在满足规则的数组组合
规则：
  A=B+2C
输入描述
 第一行输出数组的元素个数
 接下来一行输出所有数组元素  用空格隔开
输出描述
 如果存在满足要求的数
 在同一行里依次输出 规则里 A/B/C的取值 用空格隔开
 如果不存在输出0

 示例1：
   输入
   4
   2 7 3 0
   输出
   7 3 2
   说明：
    7=3+2*2
   示例2：
   输入
    3
    1 1 1
   输出
    0
    说明找不到满足条件的组合

    备注：
    数组长度在3~100之间
    数组成员为0~65535
    数组成员可以重复
    但每个成员只能在结果算式中使用一次
    如 数组成员为 [0,0,1,5]
    0出现两次允许，但结果0=0+2*0不允许  因为算式中使用了3个0

    用例保证每组数字里最多只有一组符合要求的解
'''
def f(x):
    y = {}
    for A in x:
        tmp = x.copy()
        tmp.remove(A)
        for B in tmp:
            y[(A + 2*B)]=(A,B)
    return y

while True:
    try:
        n = 3
        list1 = list(map(int,'2 7 3 0'.strip().split()))
        list2 = sorted(list(set(list1)),reverse=True)#[7, 3, 2, 0]
        for i in list2:
            tmp2 = list2.copy()
            tmp2.remove(i)
            tmp3 = list(f(tmp2).keys())
            tmp4 = list(f(tmp2).values())
            for j in range(len(tmp3)):
                if i in tmp3:
                    print(f'{i} {tmp4[j][0]} {tmp4[j][-1]}')
                    break
    except:
        print(0)
        break