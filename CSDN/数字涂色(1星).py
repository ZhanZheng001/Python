'''
题目描述
疫情过后，希望小学终于又重新开学了，三年二班开学第一天的任务是将后面的黑板报重新制作。黑板上已经写了N个正整数，同学们需要给每个数分别上一种颜色。
 3 为了让黑板报即美观又有学习意义，老师要求同种颜色的所有数都可以被这种颜色中最小的那个数整除。现在请你帮帮小朋友们，算算最少需要多少种颜色才能给这N个数进行上色。

输入描述：
第一行有一个正整数N，其中1<=N<=100。
第二行有N个int型数（保证输入数据在[1,100]范围中），表示黑板上各个正整数的值。

输出描述：
输入只有一个整数，为最少需要的颜色种数。

示例 1
输入：
3
2 4 6
输出：
1
说明：
所有数都能被2整除
```
输入：
4
2 3 4 9
输出：
2
说明：
2与4涂一种颜色，4能被2整除
3与9涂另一种颜色，9能被3整除
不能涂同一种颜色
'''
while 1:
    try:
        _ = input()
        nums = list(map(int, input().split()))

        dp = []
        while nums:
            # 取最小值 并将最小值的倍数 分为一组
            min_ = min(nums)
            ca = []
            i = 0
            while i < len(nums):
                if nums[i] % min_ == 0:
                    ca.append(nums[i])
                    nums.pop(i)
                else:
                    i += 1
            dp.append(ca)

        print(len(dp))
    except Exception as e:
        break