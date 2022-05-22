'''
双11众多商品进行打折销售，小明想购买一些自己心意的商品
但由于受购买资金限制，所以他决定从众多心意商品中购买3件
而且想尽可能的花完资金
现在请你设计一个程序帮助小明计算尽可能花费的最大资金额

输入描述
 第一行为整型数组M 数组长度小于100 数组元素记录单个商品的价格
 单个商品价格<1000
 第二行输入为购买资金的额度R
 R<100000

输出描述
 输出为满足上述条件的最大花费额度
 如果不存在满足上述条件的商品请返回-1

例子1
输入
 23,26,36,27
 78
输出
 76

例子2
    输入
     23,30,40
     26
    输出
      -1

备注：输入格式正确
'''
while True:
    try:
        M = sorted(list(map(int,'23,26,36,27'.split(','))))#[23, 26, 27, 36]
        R = int('78')#78
        res = 0
        if len(M)<3 or sum(M[:2])> R:
            print(-1)
            break
        else:
            for i in range(len(M)-2):
                for j in range(i+1,len(M)-1):
                    for k in range(j+1,len(M)):
                        if res< M[i]+M[j]+M[k] <= R:
                            res = M[i]+M[j]+M[k]
        print(res)
        break
    except:
        break