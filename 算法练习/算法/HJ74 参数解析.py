'''
在命令行输入如下命令：

xcopy /s c:\ d:\，

各个参数如下：

参数1：命令字xcopy

参数2：字符串/s

参数3：字符串c:\

参数4: 字符串d:\

请编写一个参数解析程序，实现将命令行各个参数解析出来。


解析规则：

1.参数分隔符为空格
2.对于用""包含起来的参数，如果中间有空格，不能解析为多个参数。比如在命令行输入xcopy /s "C:\program files" "d:\"时，参数仍然是4个，第3个参数应该是字符串C:\program files，而不是C:\program，注意输出参数时，需要将""去掉，引号不存在嵌套情况。
3.参数不定长
4.输入由用例保证，不会出现不符合要求的输入


输入描述：
输入一行字符串，可以有空格

输出描述：
输出参数个数，分解后的参数，每个参数都独占一行

示例1
输入：
xcopy /s c:\\ d:\\
复制
输出：
4
xcopy
/s
c:\\
d:\\

'''


while True:
    try:
        # s=input()
        s = 'l "b: 1" /kzv /yar'
        temp,res=[],[]
        for i,x in enumerate(s):
            if x=='"':
                temp.append(i)
        while temp:
            if s[temp[0]:temp[1]].find(' ')!=-1:
                a=s[temp[0]:temp[1]].replace(' ','++++')
                s=s[:temp[0]]+a+s[temp[1]+1:]
            temp.pop(0)
            temp.pop(0)
        res=s.split()
        for j in range(len(res)):
            res[j]=res[j].replace('++++',' ')
            if res[j].find('"')!=-1:
                res[j]=res[j].replace('"','')
        print(len(res))
        for k in res:
            print(k)
        break
    except:
        break