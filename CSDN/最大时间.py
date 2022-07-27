'''
题目描述
给定一个数组,里面有 6 个整数,求这个数组能够表示的最大 24 进制的时间是多少,输出这个时间,无法表示输出 invalid。

输入描述：
输入为一个整数数组,数组内有六个整数。输入整数数组长度为 6,不需要考虑其它长度,元素值为 0 或者正整数,6 个数字每个数字只能使用一次.

输出描述：
输出为一个 24 进制格式的时间,或者字符串"ivalid"
备注:输出时间格式为 xxxxx 式

示例 1
输入：0,2,3,0,5,6
输出：23:56:00

参考代码

'''
while 1:
    try:
        nums = input().split(',')

        def dfs(ids, max_, dp):
            sub = "".join([nums[i] for i in ids])
            if 0 <= int(sub) < max_ and len(sub) == 2:
                dp.append((sub, ids))
            else:
                for i in range(len(nums)):
                    if i not in ids:
                        dfs(ids+[i], max_, dp)

        def fun(max_):
            dp = []
            for i in range(len(nums)):
                dfs([i], max_, dp)
            dp = sorted(dp, key=lambda x: int(x[0]), reverse=True)
            if dp:
                for c in str(dp[0][0]):
                    nums.remove(c)
                return str(dp[0][0])

        # 取最大小时数
        h = fun(24)
        # 取最大分钟数
        m = fun(60)
        # 取最大秒数
        s = fun(60)

        if h and m and s:
            print(f"{h}:{m}:{s}")
        else:
            print("ivalid")

    except Exception as e:
        break