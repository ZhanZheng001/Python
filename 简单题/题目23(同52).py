'''
       /*
        磁盘的容量单位常用的有
        M G T
        他们之间的换算关系为 1T =1024G 1G=1024M
        现在给定n块磁盘的容量，请对他们按从小到大的顺序进行稳定排序
        例如给定5块盘的容量
        5
        1T
        20M
        3G
        10G6T
        3M12G9M
        排序后的结果为
        20M
        3G
        3M 12G 9M
        1T,10G 6T
        注意单位可以重复出现
        上述3M 12G 9M表示的容量即为 3M 12G 9M 和12M 12G相等
        输入描述、
          输入第一行包含一个整数n
          2<=n<=100 表示磁盘的个数
          接下来的n行
          每行一个字符串
          2<长度<30
          表示磁盘的容量
          由一个或多个格式为MV的子串组成
          其中m表示容量大小
          v表示容量单位
          例如20M 1T
          磁盘容量的范围1~1024的正整数
          单位 M G T
         输出n行
         表示n块磁盘容量排序后的结果

         实例
         输入
         3
         1G
         2G
         1024M
        输出
        1G
        1024M
        2G
        说明：稳定排序要求相等值保留原来位置

        示例2
        3
        2G4m
        3M2G
        1T
        输出
        3M2G
        2G4M
        1T
         */
'''
def changeToM(x):
    list1 = []
    i,j,tmp= 0,0,0
    while i < len(x):
        if x[i].isalpha():
            list1.append(f'{x[j:i]},{x[i]}')
            j = i+1
            i+=1
        else:i+=1
    for i in list1:
        num = int(i.split(',')[0])
        dan = i.split(',')[-1]
        if dan == 'M':
            tmp += num
            continue
        elif dan == 'G':
            tmp += 1024*num
            continue
        else:
            tmp += 1024*1024*num
            continue
    return tmp

while True:
    try:
        # n = int(input())
        n = 3
        # list1=[]
        # for i in range(n):
        #     list1.append(input().strip())
        list1 = ['1G', '2G', '1024M']
        dict1 = dict()
        for i in range(len(list1)):
            dict1[list1[i]] = changeToM(list1[i])
        list2 = sorted(dict1.items(),key=lambda x:x[1])
        # print(list2)
        for i in list2:
            print(i[0])
        break
    except:
        break