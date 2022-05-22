'''
    给出一个只包含字母的字符串,不包含空格,统计字符串中各个子字母(区分大小写)出现的次数,并按照字母出现次数从大到小
    的顺序输出各个字母及其出现次数如果次数相同,按照自然顺序排序,且小写字母在大写字母之前

    输入描述:
      输入一行仅包含字母的字符串
    输出描述:
      按照字母出现次数从大到小的顺序输出各个字母和字母次数,
      用英文分号分割,
      注意末尾的分号
      字母和次数中间用英文冒号分隔

    示例:
        输入: xyxyXX
        输出:x:2;y:2;X:2;
    说明:每个字符出现的次数为2 故x排在y之前
    而小写字母x在大写X之前
    示例2:
        输入:
         abababb
        输出:
            b:4;a:3
        说明:b的出现个数比a多 故排在a前
'''
while True:
    try:
        # str1 = input()
        str1 = 'xyxyXXabababb'
        dict1,dict2 = dict(),dict()
        list1,list2 = list(),list()
        for i in set(str1):
            if i.islower():
                dict1[i] = str1.count(i)
            else:
                dict2[i] = str1.count(i)
        list1 = sorted(dict1.items(),key=lambda x:x[0])#先按自然序升序
        list2 = sorted(dict2.items(), key=lambda x: x[0])
        list1 = sorted(list1,key=lambda x:x[1], reverse=True)#再按照数量倒序
        list2 = sorted(list2,key=lambda x:x[1], reverse=True)
        for i in list1+list2:
            print(f'{i[0]}:{i[1]}',end=';')
        break
    except:
        break