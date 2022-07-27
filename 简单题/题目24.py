'''
    /*
    身高从低到高
    身高相同体重从轻到重
    体重相同维持原来顺序
    输入
    4
    100 100 120 130
    40 30 60 50
    输出：
    2 1 3 4
    输入
    3
    90 110 90
    45 60 45
    输出
    1 3 2
     */
'''

while True:
    try:
        n= int('4')
        list1 = list(map(int, '100 100 120 130'.split(' ')))
        list2 = list(map(int, '40 30 60 50'.split(' ')))
        tmp = []
        for i in range(n):
            tmp.append([i+1,list1[i],list2[i]])
        tmp.sort(key=lambda x:(x[1],x[2]))
        for i in tmp:
            print(i[0],end=' ')
        break
    except:
        break