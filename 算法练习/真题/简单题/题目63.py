'''
    给定两个字符集合,一个是全量字符集,一个是已占用字符集,已占用字符集中的字符不能再使用,要求输出剩余可用字符集
输入描述
     1. 输入一个字符串 一定包含@
     @前为全量字符集  @后的为已占用字符集
     2. 已占用字符集中的字符
     一定是全量字符集中的字符
     字符集中的字符跟字符之间使用英文逗号隔开
     3. 每个字符都表示为字符+数字的形式
      用英文冒号分隔
      比如a:1标识一个a字符
     4. 字符只考虑英文字母，区分大小写
      数字只考虑正整型 不超过100
     5. 如果一个字符都没被占用 @标识仍存在
     例如 a:3,b:5,c:2@
输出描述：
       输出可用字符集,不同的输出字符集之间用回车换行
       注意 输出的字符顺序要跟输入的一致,不能输出b:3,a:2,c:2,如果某个字符已全部占用 则不需要再输出
示例一：
       输入:a:3,b:5,c:2@a:1,b:2
       输出:a:2,b:3,c:2
       说明：全量字符集为三个a，5个b，2个c,已占用字符集为1个a，2个b
       由于已占用字符不能再使用,因此剩余可用字符为2个a，3个b，2个c,因此输出a:2,b:3,c:2
'''
while True:
    try:
        str1,str2 = 'a:3,b:5,c:2@a:1,b:2'.strip().split('@')
        list1,list2 = str1.split(','),str2.split(',')
        list_a,list_an,list_b,list_bn = [],[],[],[]
        for i in range(len(list1)):
            list_a.append(list1[i][0])
            list_an.append(int(list1[i][2]))    #['a', 'b', 'c'] [3, 5, 2]
        for i in range(len(list2)):
            list_b.append(list2[i][0])
            list_bn.append(int(list2[i][2]))    #['a', 'b'] [1, 2]

        for i in range(len(list_b)):
            tmp_index = list_a.index(list_b[i])
            list_an[tmp_index] -= list_bn[i]    #['a', 'b', 'c'] [2, 3, 2]
        for i in range(len(list_a)):
            list_a[i] = f'{list_a[i]}:{list_an[i]}'
        print(','.join(list_a))
        break
    except:
        break