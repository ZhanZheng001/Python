'''
题目描述
查找两个字符串 a,b 中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
输入两个字符串
返回重复出现的字符

示例1
输入：

abcdefghijklmnop
abcsafjklmnopqrstuvw
1
2
输出：

jklmnop
1
示例2
输入：

abc
defghijklmnop
1
2
输出：


1
参考代码
我们在 a 字符串上确定一个 字符串范围，拿这个子串在 b 字符串上匹配，看是否存在相同的子串；
如果存在相同的子串，我们向右移动边界来尝试比较更长的子串；
如果不满足将左边界右移，然后重复以上的操作。

最后在 缓存中找出最长的公共子串输出。


'''
while 1:
    try:
        a = input()
        b = input()

        lens_a = len(a)
        lens_b = len(b)

        if lens_a > lens_b:
            a, b = b, a
            lens_a, lens_b = lens_b, lens_a

        dp = []
        i = 0
        j = 1
        while j <= lens_a:
            if a[i:j] in b:
                dp.append(a[i: j])
                j += 1
            else:
                i += 1
                j = i + 1
        if dp:
            dp = sorted(dp, key=lambda x: len(x), reverse=True)
            print(dp[0])
        else:
            print("")
    except Exception as e:
        break