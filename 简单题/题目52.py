'''
磁盘的容量单位有M,G,T这三个等级
他们之间的换算关系为
1T=1024G
1G=1024M
现在给定N块磁盘的容量
  请对他们按从小到大的顺序进行稳定排序
  例如给定5块盘容量
  1T,20M,3G,10G6T,3M12G9M
排序后的结果为20M,3G,3M12G9M,1T,10G6T

注意单位可以重复出现
上述3M12G9M为 3M+12G+9M和 12M12G相等

输入描述:
输入第一行包含一个整数N
2<=N<=100 ,表示磁盘的个数
接下来的N行每行一个字符串 长度 (2<l<30)
表示磁盘的容量
有一个或多个格式为 mv的子串组成
其中m表示容量大小 v表示容量单位
例如

磁盘容量m的范围 1~1024正整数
容量单位v的范围包含题目中提到的M,G,T

输出描述:
 输出N行
 表示N块磁盘容量排序后的结果

 示例1:
 输入
     3
     1G
     2G
     1024M

 输出
    1G
    1024M
    2G

说明 1G和1024M容量相等,稳定排序要求保留他们原来的相对位置
故1G在1024M前

 示例二:
 输入
      3
      2G4M
      3M2G
      1T

  输出
    3M2G
    2G4M
    1T
    说明1T大于2G4M大于3M2G

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
        for i in list2:
            print(i[0])
        break
    except:
        break