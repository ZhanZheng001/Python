'''
题目描述
华为商城举办了一个促销活动，如果某顾客是某一秒内最早时刻下单的顾客（可能是多个人），则可以获取免单。请你编程计算有多少顾客可以获取免单。

输入为 n 行数据，每一行表示一位顾客的下单时间
以（年-月-日时-分-秒.毫秒） yyyy-MM-ddHH:mm:ss.fff 形式给出。
0<n<50000
2000<yyyy<2020
0<MM<=12
0<dd<=28
0<=HH<=23
0<=mm<=59
0<=ss<=59
0<=fff<=999
所有输入保证合法。

输出一个整数，表示有多少顾客可以获取免单。

示例 1
输入：

3
2019-01-01 00:00:00.001
2019-01-01 00:00:00.002
2019-01-01 00:00:00.003
1
2
3
4
输出：

1
1
示例 2
输入：

3
2019-01-01 08:59:00.123
2019-01-01 08:59:00.123
2018-12-28 10:08:00.999
1
2
3
4
输出：

3
1
示例 3
输入：

5
2019-01-01 00:00:00.004
2019-01-01 00:00:00.004
2019-01-01 00:00:01.006
2019-01-01 00:00:01.006
2019-01-01 00:00:01.005
1
2
3
4
5
6
输出：

3
1
提示
样例 1 中，三个订单都是同一秒内下单，只有第一个订单最早下单，可以免单。

样例 2 中，前两个订单是同一秒内同一时刻（也是最早）下单，都可免单，第三个订单是当前秒内唯一一个订单（也是最早），也可免单。

样例 3 中，前两个订单是同一秒内同一时刻（也是最早）下单，第三第四个订单不是当前秒内最早下单，不可免单，第五个订单可以免单。

参考代码
把订单时间字符串（2019-01-0100:00:00.001）按小数点分为第一部分和第二部分，第一部分是整数部分的字符串，第二部分是小数部分的字符串。
建立一个 map，以整数部分为 key，小数部分和第一个下单的人的个数为 value，记录下每秒钟第一个下单的人。
统计 map 中所有的每秒第一个下单的人数。


'''
while 1:
    try:
        size = int(input())
        order_time = [input() for _ in range(size)]

        dp = {}

        for ct in order_time:
            _ct, mint = ct.split('.')
            if _ct in dp:
                if dp[_ct]["val"] == mint:
                    dp[_ct]["count"] += 1
                elif dp[_ct]["val"] > mint:
                    # 最早时间刷新，同时刷新计数
                    dp[_ct]["val"] = mint
                    dp[_ct]["count"] = 1
            else:
                # 首次出现的时间点，计数为1
                dp[_ct] = {
                    "val": mint,
                    "count": 1
                }

        total = sum(v["count"] for v in dp.values())
        print(total)
    except Exception as e:
        break