'''
题目描述
一群大雁往南飞，给定一个字符串记录地面上的游客听到的大雁叫声，请给出叫声最少由几只大雁发出。

具体的:

大雁发出的完整叫声为”quack“，因为有多只大雁同一时间嘎嘎作响，所以字符串中可能会混合多个”quack”。
大雁会依次完整发出”quack”，即字符串中’q’ ,‘u’, ‘a’, ‘c’, ‘k’ 这5个字母按顺序完整存在才能计数为一只大雁。如果不完整或者没有按顺序则不予计数。
如果字符串不是由’q’, ‘u’, ‘a’, ‘c’, ‘k’ 字符组合而成，或者没有找到一只大雁，请返回-1。
输入描述：
一个字符串，包含大雁quack的叫声。1 <= 字符串长度 <= 1000，字符串中的字符只有’q’, ‘u’, ‘a’, ‘c’, ‘k’。

输出描述：
大雁的数量

示例 1
输入：
quackquack

输出：
1
'''
# ![](https://myimage-zz.oss-cn-shenzhen.aliyuncs.com/img/202206051050076.png)
# 模拟几只大雁可能是按上面的顺序发声，收集到的叫声可能是下面的字符串：
# qququaauqccauqkkcauqqkcauuqkcaaukccakkck
#
# 怎么确认最少的个数呢，我们找到第一个q和第一个k下标，在这个范围内存在q的数量且q可以在后面的字符串中构成完成的quack时，就可以记为一个大雁
while 1:
    try:
        chars = input()

        dp = []

        def dfs(nums):
            # 确定一个有效的叫声范围
            s = 0
            e = 0
            for c in "uack":
                e += nums[e:].index(c)
            e += 1

            dct = {
                "q": 0,
                "u": 0,
                "a": 0,
                "c": 0,
                "k": 0,
            }
            k = 0
            while k < len(nums):
                if nums[k] == "q":
                    if s <= k <= e:
                        dct["q"] += 1
                else:
                    dct[nums[k]] += 1
                k += 1

            # 如果其他字母计数小于
            dp.append(min(dct.values()))

        i = 0
        while "q" in chars[i:]:
            i = chars.index("q")
            dfs(chars[i:])
            chars = chars[i+1:]

        print(max(dp))
    except Exception as e:
        break
