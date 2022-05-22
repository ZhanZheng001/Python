'''
/*
    给定一个字符串
    只包含大写字母
    求在包含同一字母的子串中
    长度第K长的子串
    相同字母只取最长的子串

    输入
     第一行 一个子串 1<len<=100
     只包含大写字母
     第二行为k的值

     输出
     输出连续出现次数第k多的字母的次数

     例子：
     输入
             AABAAA
             2
     输出
             1
       同一字母连续出现最多的A 3次
       第二多2次  但A出现连续3次

    输入

    AAAAHHHBBCDHHHH
    3

    输出
    2

//如果子串中只包含同一字母的子串数小于k

则输出-1

 */
'''
while True:
    try:
        str1 = 'AAAAHHHBBCDHHHH'.strip() +' '
        k = 3
        str2=''
        i=0
        while i < len(str1) - 1:
            if str1[i] == str1[i + 1]:
                str2 += str1[i]
                i += 1
            else:
                str2 += f'{str1[i]} '
                i += 1      #'AAAA HHH BB C D HHHH'
        list1 = str2.strip(' ').split(' ')  #['AAAA', 'HHH', 'BB', 'C', 'D', 'HHHH']
        dict1 = {}
        for i in list1:
            dict1[i[0]]= len(i)#{'A': 4, 'H': 4, 'B': 2, 'C': 1, 'D': 1}
        tmp = sorted(dict1.items(),key= lambda x:x[1],reverse=True)#[('A', 4), ('H', 4), ('B', 2), ('C', 1), ('D', 1)]
        if k > len(tmp):
            print(-1)
        else:
            print(tmp[k-1][1])

        break
    except:
        break