'''
给定一个正整数数组,检查数组中是否存在满足规则的数组组合
规则：A=B+2C
输入描述:第一行输出数组的元素个数;接下来一行输出所有数组元素  用空格隔开
输出描述:如果存在满足要求的数;在同一行里依次输出 规则里 A/B/C的取值 用空格隔开;如果不存在输出0
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
while True:
    try:
        n = 4 #input()
        list1 = sorted(list(map(int,"2 7 3 0".strip().split(" "))),reverse=True)
        res = "0"
        for A in range(n-2):
            for B in range(A+1,n-1):
                for C in range(A+1,n):
                    if list1[A] == list1[B] + 2 * list1[C] and B != C:
                        res = f"{list1[A]} {list1[B]} {list1[C]}"
                        break
        print(res)
        break
    except:
        break