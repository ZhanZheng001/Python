'''
题目描述
solo 从小就对英文字母非常感兴趣，尤其是元音字母(a,e,i,o,u,A,E,I,O,U)，他在写日记的时候都会把元音字母写成大写的，辅音字母则都写成小写，虽然别人看起来很别扭，但是 solo 却非常熟练。你试试把一个句子翻译成 solo 写日记的习惯吧。

输入描述：
输入一个字符串 S(长度不超过 100，只包含大小写的英文字母和空格)。

输出描述：
按照 solo 写日记的习惯输出翻译后的字符串 S。

示例 1
输入： Intheend,it’snottheyearsinyourlifethatcount.It’sthelifeinyouryears.
输出： InthEEnd,It’snOtthEyEArsInyOUrlIfEthAtcOUnt.It’sthElIfEInyOUryEArs.

参考代码
可以使用 哈希表 或者 字符串保存小写的元音字母，哈希表的计算速度更快；
我们使用列表保存处理后的字母，没有使用 += 对字符串进行拼接；
字符串是不可变类型 频繁的拼接操作会不断地生成新的空间存储新字符串，性能不佳。


'''
bct = "aeiou"

while 1:
    try:
        s = input()

        dp = list(s)
        for i, c in enumerate(s):
            if c in bct:
                dp[i] = c.upper()
            else:
                dp[i] = c.lower()

        print("".join(dp))
    except Exception as e:
        break