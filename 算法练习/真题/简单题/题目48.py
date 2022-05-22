'''
        给定一个元素类型为小写字符串的数组
        请计算两个没有相同字符的元素长度乘积的最大值
        如果没有符合条件的两个元素返回0

        输入描述
          输入为一个半角逗号分割的小写字符串数组
          2<= 数组长度 <=100
          0< 字符串长度 <=50
        输出描述
          两个没有相同字符的元素长度乘积的最大值

        示例一
          输入
            iwdvpbn,hk,iuop,iikd,kadgpf
          输出
            14
          说明
           数组中有5个元组  第一个和第二个元素没有相同字符
           满足条件 输出7*2=14
'''
while True:
    try:
        list1 = 'iwdvpbn,hk,iuop,iikd,kadgpf'.strip().split(',')#['iwdvpbn', 'hk', 'iuop', 'iikd', 'kadgpf']
        tmp = []
        for i in range(len(list1)-1):
            for j in range(i+1,len(list1)):
                if set(list1[i]).isdisjoint(set(list1[j])):
                    tmp.append(len(list1[i]*len(list1[j])))
        print(max(tmp))
        break
    except:
        break