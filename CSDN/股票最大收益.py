'''
题目描述
假设知道某段连续时间内股票价格，计算通过买入卖出可获得的最大收益。

输入一个大小为 n 的数 price(p1,p2,p3,p4…….pn),pi 是第天的股票价格。

pi 的格式为股票价格(非负整型)加上货币单位 Y 或者 S,其中 Y 代表人民币,S 代表美元,这里规定 1 美元可以兑换 7 人民币。

Pi 样例 1： 123Y 代表 123 元人民币
pi 样例 2： 123S 代表 123 元美元,可兑换 861 人民币

假设你可以在任何一天买入或者卖出胶票,也可以选择放弃交易,请计其在交易周期 n 天内你能获得的最大收(以人民币计算。

输入描述：
输入一个包含交易周期内各天股票价格的字符串，以空格分隔。不考虑输入异常情况。

输出描述：
输出一个整型数代表在交易周期 n 天内你能获得的最大收益， n 不能超过 10000
备注：股票价格只会用 Y 人民币或 S 美元进行输入，不考虑其他情况。

示例 1
输入：2Y 3S 4S 6Y 8S
输出：76


'''
# 参考代码
# 方便计算需要将输入转换为统一货币，可以实时计算也可以提前生成新数组；
# 最大收益 是在最低点买入，最高点卖出；
# 遍历数组 找到最小值，然后和最小值后面出现的最大值 求差值 即最大收益；

def to_rmb(n):
    if n[-1] == "Y":
        return int(n[:-1])
    else:
        return int(n[:-1])*7


while 1:
    try:
        nums = list(map(to_rmb, input().split()))

        if not nums:
            print(0)
            break

        dp = []
        # 最大收益
        max_ = 0
        # 当前最小值
        min_ = nums[0]
        before_ = nums[0]
        for c in nums:
            if before_ > c:
                dp.append(max_)
                min_ = c
                max_ = 0
            else:
                min_ = min(min_, c)
                max_ = max(max_, c - min_)
            before_ = c

        dp.append(max_)
        print(sum(dp))
    except Exception as e:
        break