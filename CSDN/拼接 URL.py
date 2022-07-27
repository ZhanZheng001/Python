'''
题目描述
给定一个 URL 前缀和 URL 后缀,需要将其连接为一个完整的 URL,如果前缀结尾和后缀开头都没有“/” ,则需自动补上“/”连接符, 如果前缀结尾和后缀开头都有“/”，需自动去重。

例如:
1)前缀:/a;后缀:/b;连接后 URL 为: /a/b,
2)前缀: /a/;后缀:/b; 连接后 URL 为:/a/b,
3)前缀: /a;后缀:b;连接后 URL 为:/a/b,
4)前缀为空;后缀为空;连接后 URL 为:/

约束: 不用考虑前后缀 URL 不合法情况

输入描述：
URL 前缀（一个小于 100 的字符串）， URL 后缀（一个小于 100 的字符串）
输出描述：
拼接后的 URL.

示例 1
输入：/a /b
输出：/a/b

示例 2
输入：/a/ /b
输出：/a/b

示例 3
输入：/a b
输出：/a/b

示例 4
输入：
输出：/
'''
while 1:
    try:
        sto = input()
        st = sto.split()
        a = ""
        b = ""
        if len(st) == 1:
            # 判断是 前缀还是后缀
            if sto.startswith(" "):
                b = st[0]
            else:
                a = st[0]
        elif len(st) == 2:
            a = st[0]
            b = st[1]
        else:
            print("/")
            continue

        # 我们要求 前缀不由 / 结尾
        # 结尾有多个 /
        while a.endswith("/"):
            a = a[:-1]

        # 开头有多个 /
        while b.startswith("/"):
            b = b[1:]

        # 我们要求 后缀由 / 开始
        b = f"/{b}"

        print(a+b)
    except Exception as e:
        break