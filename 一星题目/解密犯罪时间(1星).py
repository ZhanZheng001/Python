'''
题目描述
警察在侦破一个案件时，得到了线人给出的可能犯罪时间，形如 “HH:MM” 表示的时刻。
根据警察和线人的约定，为了隐蔽，该时间是修改过的。
解密规则为：利用当前出现过的数字，构造下一个距离当前时间最近的时刻，则该时间为可能的犯罪时间。
每个出现数字都可以被无限次使用。
输入描述：
形如HH:MM字符串，表示原始输入。
输出描述：
形如HH:MM的字符串，表示推理处理的犯罪时间。
备注
1.可以保证现任给定的字符串一定是合法的。
例如，“01:35”和“11:08”是合法的，“1:35”和“11:8”是不合法的。
2.最近的时刻可能在第二天。

示例 1
输入：20:12
输出：20:20

示例 2
输入：23:59
输出：22:22

示例 3
输入：12:58
输出：15:11

示例 4
输入：18:52
输出：18:55
'''
while 1:
    try:
        hh, mm = "12:58".split(":")
        set1 = set(list(hh) + list(mm)) #{'2', '8', '1', '5'}
        ori = hh+mm #1258
        dp = []
        def dfs(hm_):
            lens = len(hm_)
            if lens == 2 and hm_ > "23":
                return
            elif lens == 3 and (hm_ > "235" or hm_[2] > "5"):
                return
            elif lens >= 4:
                if hm_ > ori:
                    dp.append(hm_)
                else:
                    dp.append("1"+hm_)
            else:
                for c in set1:
                    dfs(hm_+c)
        for c in set1:
            if c <= "2":
                dfs(c)
        ret = sorted(dp, key=lambda x: int(x))[0] #['1511', '1512', '1515', '1518', '1521', '1522', '1525', '1528', '1551',...]
        if len(ret) == 5:
            print(f"{ret[1:3]}:{ret[3:]}")
        else:
            print(f"{ret[:2]}:{ret[2:]}")
        break
    except Exception as e:
        break