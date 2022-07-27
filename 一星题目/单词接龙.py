'''
单词接龙的规则:是可用于接龙的单词 首字母必须要与前一个单词的尾字母相同,当存在多个首字母相同的单词时，取长度最长的单词
如果长度也相等，则取字典序最小的单词,已经参与接龙的单词不能重复使用,现给定一组全部由小写字母组成的单词数组
并指定其中一个单词为起始单词,进行单词接龙,请输出最长的单词串,单词串是单词拼接而成的中间没有空格
输入描述
输入第一行为一个非负整数
表示起始单词在数组中的索引k
0<=k<N
输入的第二行为非负整数N
接下来的N行分别表示单词数组中的单词
输出描述，
输出一个字符串表示最终拼接的单词串
示例
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
说明 先确定起始单词word 在接dword
剩余dd da dc 则取da

示例2
4
6
word
dd
da
dc
dword
d

输出
dwordda

单词个数1<N<20
单个单词的长度  1~30
'''
# def next(x,y):
#     tmp = []
#     for i in y:
#         if x[-1] == i[0]:
#             tmp.append(i)
#         else:
#             continue
#     if tmp:
#         max1=0
#         tmp2=[]
#         for i in tmp:
#             if len(i)> max1:
#                 max1 = len(i)
#         for i in tmp:
#             if len(i)==max1:
#                 tmp2.append(i)
#         tmp2.sort()
#         return tmp2[0]
#     else:
#         return ''
#
# while True:
#     try:
#         k,n = int('0'),int('6')
#         # list1 = []
#         # for i in range(n):
#         #     list1.append(input().strip())
#         list1 = ['word', 'dd', 'da', 'dc', 'dword', 'd']
#         str1 = list1[k]#word
#         list1.pop(k)#['dd', 'da', 'dc', 'dword', 'd']
#         res = [str1]
#         while next(str1,list1):
#             tmp = next(str1,list1)
#             res.append(tmp)
#             str1 = tmp
#             list1.remove(tmp)
#         print(''.join(res))
#         break
#     except:
#         break
while 1:
    try:
        k = int("0")
        n = int("6")
        # nums = [input() for _ in range(n)]
        nums = ['word', 'dd', 'da', 'dc', 'dword', 'd']
        dp = [nums.pop(k)]# 接龙结果
        while len(nums):
            cache = [] # 备选单词
            for w in nums:
                if dp[-1][-1] == w[0]: #上一个单词的尾字符 == 当前单词的首字符
                    cache.append(w)
            if cache:
                cache = sorted(cache, key=lambda x: (-len(x), x))
                next_ = cache[0]
                nums.remove(next_)
                dp.append(next_)
            else:
                break
        print("".join(dp))
        break
    except Exception as e:
        break