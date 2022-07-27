'''
        /*
            输入一个字符串仅包含大小写字母和数字
            求字符串中包含的最长的非严格递增连续数字序列长度
            比如：
                12234属于非严格递增数字序列
            示例：
            输入
                abc2234019A334bc
            输出
                4
            说明：
                2234为最长的非严格递增连续数字序列，所以长度为4

                aaaaaa44ko543j123j7345677781
                aaaaa34567778a44ko543j123j71
                345678a44ko543j123j7134567778aa
         */

'''
while True:
    try:
        a = list('abc2234019A334bc'.strip())
        for i in range(len(a)):
            if a[i].isalpha():
                a[i] = ' '
        res=''.join(a).strip().split()
        tmp = []
        for i in res:
            for j in range(0,len(i)-1):
                for h in range(j+1,len(i)+1):
                    if i[j:h] == ''.join(sorted(list(i[j:h]))):
                        tmp.append(len(i[j:h]))
        print(max(tmp))
        break
    except:
        break
