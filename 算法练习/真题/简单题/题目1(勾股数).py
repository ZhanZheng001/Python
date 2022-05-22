'''
如果三个正整数A B C ,A²+B²=C²则为勾股数
 如果ABC之间两两互质，即A与B,A与C,B与C均互质没有公约数，
 则称其为勾股数元组。
请求出给定n m 范围内所有的勾股数元组
输入描述
  起始范围 1<n<10000    n<m<10000
输出目描述
   abc 保证a<b<c输出格式  a b c
   多组勾股数元组 按照a升序b升序 c升序的排序方式输出。
   给定范围内，找不到勾股数元组时，输出  Na

 案例
  输入
   1
   20
  输出
   3 4 5
   5 12 13
   8 15 17

  输入
    5
    10
  输出
    Na
'''
def f1(x,y,z):
    if x*x+y*y==z*z:
        return True
    else:
        return False
def f2(x,y,z):
    for i in range(2,z+1):
        if x%i==0 and y%i==0:
            return False
        elif y%i==0 and z%i==0:
            return False
        elif x%i==0 and z%i==0:
            return False
        else:
            continue
    return True
while True:
    try:
        n = int('1')
        m = int('20')
        res = []
        for A in range(n,m-1):
            for B in range(A+1,m):
                for C in range(B+1,m+1):
                    if f1(A,B,C) and f2(A,B,C):
                        res.append(f'{A} {B} {C}')
                        break
                    else:
                        continue
        if res:
            for i in res:
                print(i)
        else:
            print('Na')
        break
    except:
        break