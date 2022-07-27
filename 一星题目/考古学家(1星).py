'''
题目描述
有一大堆墓碑碎片，每个碎片就是一个字符串，让你给出排列组合的所有可能，要去重。
比如 a b c 这么3块墓碑,排列组合有：
abc acb bac bca cab cba 这么多种。

输入描述：
输入第一行表示墓碑碎片
输出描述：
输出不重复的墓碑组合

示例 1
输入：a b ab
输出：abab aabb baab baba abba
墓碑是 a b ab ，则 要记得去重，结果是 abab aabb baab baba abba , 其实还有一个 abab,因为和第一个重了，所以要去掉。
'''
while 1:
    try:
        list1 = "a b ab".split()
        dp = []
        def dfs(sub): # 对碎片进行组合
            if len(sub) == len(list1):
                t = "".join(sub)
                if t not in dp:  # 剔除重复的结果, 比如 abab 可以是 a + b + ab  或 ab + a + b
                    dp.append(t)
            else:
                for c in list1:
                    if c not in sub: # 剔除重复的碎片
                        dfs(sub + [c])
        for c in list1:
            dfs([c])
        print(" ".join(dp))
        break
    except Exception as e:
        break
