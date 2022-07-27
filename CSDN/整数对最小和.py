'''
题目描述
给定两个整数数组 array1、 array2，数组元素按升序排列。假设从 array1、 array2 中分别取出一个元素可构成一对元素，现在需要取出 k 对元素，并对取出的所有元素 求和，计算和的最小值

注意：两对元素如果对应于 array1、 array2 中的两个下标均相同，则视为同一对元素。

输入描述：
输入两行数组 array1、 array2，每行首个数字为数组大小 size(0 < size <= 100);
0 < array1[i] <= 1000 0 < array2[i] <= 1000

接下来一行为正整数 k
0 < k <= array1.size() * array2.size()

输出描述：
满足要求的最小和

示例 1
输入:
3 1 1 2
3 1 2 3
2
输出：
4

参考代码

'''
while 1:
    try:
        array1 = list(map(int, input().split()))[1:]
        array2 = list(map(int, input().split()))[1:]
        k = int(input())

        dp = []
        for i in array1:
            for j in array2:
                dp.append(i+j)

        dp = sorted(dp)
        print(sum(dp[:2]))
    except Exception as e:
        break