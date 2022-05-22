'''
        单词接龙的规则是:可用于接龙的单词首字母必须要与前一个单词的尾字母相同,当存在多个首字母相同的单词时,取长度最长的单词
        如果长度也相等则取词典序最小的单词,已经参与接龙的单词不能重复使用
        现给定一组全部由小写字母组成的单词数组
        并指定其中的一个单词为起始单词
        进行单词接龙
        请输出最长的单词串
        单词串是由单词拼接而成 中间没有空格

        输入描述：
            输入的第一行为一个非负整数
            表示起始单词在数组中的索引k  0<=k<=n
            第二行输入的是一个非负整数表示单词的个数n
            接下来的n行分别表示单词数组中的单词

        输出描述：
            输出一个字符串表示最终拼接的字符串

        示例1：
        输入
          0
          6
          word
          dd
          da
          dc
          dword
          d

        输出
          worddwordda

        说明：
        先确定起始单词word
        再确定d开头长度最长的单词dword
        剩余以d开头且长度最长的由 da dd dc
        则取字典序最小的da
        所以最后输出worddwordda

        示例二：
        输入：
            4
            6
            word
            dd
            da
            dc
            dword
            d
         输出：
         dwordda
'''
def next(x,y):
    tmp = []
    for i in y:
        if x[-1] == i[0]:
            tmp.append(i)
        else:
            continue
    if tmp:
        max1=0
        tmp2=[]
        for i in tmp:
            if len(i)> max1:
                max1 = len(i)
        for i in tmp:
            if len(i)==max1:
                tmp2.append(i)
        tmp2.sort()
        return tmp2[0]
    else:
        return ''

while True:
    try:
        k,n = int('0'),int('6')
        # list1 = []
        # for i in range(n):
        #     list1.append(input().strip())
        list1 = ['word', 'dd', 'da', 'dc', 'dword', 'd']
        str1 = list1[k]#word
        list1.pop(k)#['dd', 'da', 'dc', 'dword', 'd']
        res = [str1]
        while next(str1,list1):
            tmp = next(str1,list1)
            res.append(tmp)
            str1 = tmp
            list1.remove(tmp)
        print(''.join(res))
        break
    except:
        break
