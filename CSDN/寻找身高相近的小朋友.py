'''
题目描述
小明今年升学到小学一年级，来到新班级后发现其他小朋友们身高参差不齐，然后就想基于各小朋友和自己的身高差对他们进行排序，请帮他实现排序。
输入描述：
第一行为正整数 H 和 N，0<H<200，为小明的身高，0<N<Hi<200（1<=i<=N），且 N 个正整数各不相同。
输出描述：
输出排序结果，各正整数以空格分割。和小明身高差绝对值最小的小朋友排在前面，和小明身高差绝对值最大的小朋友排在最后，如果两个小朋友和小明身高差一样，则个子较小的小朋友排在前面。

示例 1
输入：

100 10
95 96 97 98 99 101 102 103 104 105
1
2
输出：

99 101 98 102 97 103 96 104 95 105
1
参考代码
第二行输入的是需要比较同学的身高；
abs(x-H) 计算小明与比较同学的身高差，作为第一排序条件；
x 作为第二排序条件，当身高差一致时按被比较同学的身高排序；
由小到大排序，sorted 默认由小到大；


'''
while 1:
    try:
        H, m = map(int, input().split())
        nums = list(map(int, input().split()))

        nums = sorted(nums, key=lambda x: (abs(x-H), x))
        print(" ".join(map(str, nums)))
    except:
        break

# 或

while 1:
    try:
        H, m = map(int, input().split())
        nums = list(map(int, input().split()))

        nums = sorted(nums, key=lambda x: (abs(x-H), x))
        for i in nums:
            print(i, end=" ")
    except:
        break