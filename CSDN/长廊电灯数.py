'''
题目描述
一条长廊里依次装有 n(1 ≤ n ≤ 65535)盏电灯，从头到尾编号 1、 2、 3、 …n-1、 n。每盏电灯由一个拉线开关控制。开始，电灯全部关着。

有 n 个学生从长廊穿过。
第一个学生把号码凡是 1 的倍数的电灯的开关拉一下；
接着第二个学生把号码凡是 2 的倍数的电灯的开关拉一下；
接着第三个学生把号码凡是 3的倍数的电灯的开关拉一下；
如此继续下去，最后第 n 个学生把号 码凡是 n 的倍数的电灯的开关拉一下。
n 个学生按此规定走完后，长廊里电灯有几盏亮着。

注：电灯数和学生数一致。

输入描述：
电灯的数量
输出描述：
亮着的电灯数量

示例 1
输入：3
输出：1

示例 2
输入：4
输出：2

初始值：[False, False, False, False, False]
第一个学生：[False, True, True, True, True]
第二个学生：[False, True, False, True, False]
第三个学生：[False, True, False, False, False]
第四个学生：[False, True, False, False, True]

参考代码
我们 以一个包含 n+1 个元素值为 False 的数组 表示初始的电灯状态；
为方便计算我们使用 n+1 个元素，第0个元素始终为 False，不影响最终结果；
False 表示灯关着；
True 表示灯亮着；
遍历数组更新电灯的状态；
最后 sum 数组 就是电灯亮着的数量。


'''
while 1:
    try:
        n = int(input())
        base = [False] * (n+1)

        for i in range(1, n+1):
            for j in range(1, n+1):
                index = j*i
                if index > n:
                    break
                else:
                    base[index] = not base[index]
        print(sum(base))

    except Exception as e:
        break