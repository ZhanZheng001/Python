'''
题目描述
将一段压缩后的字符串解压缩，并且排序输出

解压规则：
每个字符串后面跟随一个数字，表示这个字符串的重复次数。例如，“a5”解压缩的结果为“aaaaa”；“abc3”解压缩后的结果为“abcabcabc”。

排序规则：
1、根据每个字符串的重复次数升序排序，然后输出结果。例如，“a3b2”，输出的结果为“bbaaa”。
2、如果字符重复次数一样，则根据 ASCII 编码顺序做升序排序，然后输出结果。例如，“b2a2”，输出的结果为“aabb”

输入描述：
输入的原始字符串仅包含字母和数字
输出描述：
输出的结果字符串仅包含字母

示例 1
输入： a11b2bac3bad3abcd2
输出： bbabcdabcdbacbacbacbadbadbadaaaaaaaaaaa

参考代码
主要完成两个功能 生成子串 和 原始串排序；

对输入的字符串进行拆分，分解成 字符+数值的 数组；
对数组排序；
对排序后的字符解码；
使用 join 合并子串；

'''
while 1:
    try:
        nums = input()

        lens = len(nums)
        dp = []
        key = ""
        i = 0
        j = 1
        # 拆分字符串
        while j < lens:
            if "a" <= nums[i:j] <= "z" or "A" <= nums[i:j] <= "Z":
                key += nums[i:j]
                i += 1
                j += 1
            else:
                if nums[i:j].isdigit():
                    j += 1
                else:
                    dp.append((key, int(nums[i:j-1])))
                    key = nums[j-1:j]
                    i = j
                    j += 1
        else:
            if nums[i:j].isdigit():
                dp.append((key, int(nums[i:])))
            else:
                dp.append((key+nums[i:j], 1))

        # 排序
        dp = sorted(dp, key=lambda x: x[1])

        print("".join([key*count for key, count in dp]))
    except Exception as e:
        break