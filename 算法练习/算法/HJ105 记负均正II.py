'''
描述
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾，请使用while(cin>>)读入
数据范围小于1e6
输入描述：
输入任意个整数，每行输入一个。

输出描述：
输出负数个数以及所有非负数的平均值

示例1
输入：
-13
-4
-7
复制
输出：
3
0.0
'''
n=[]
while True:
    try:
        n.append(int(input()))
    except:
        break
print(n)
z,f=[],[]
for i in n:
    if i>=0:
        z.append(i)
    else:
        f.append(i)
print(len(f))
print(round(sum(z)/len(z),1) if z else 0.0)
