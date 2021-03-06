'''
题目描述
给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。

输入描述：

输入为两行，第一行为参数K，第二行为字符串S。

输出描述：

输出转换后的字符串。

示例 1
输入：

3
12abc-abCABc-4aB@
1
2
输出：

12abc-abc-ABC-4aB-@
1
参考代码

'''
while 1:
    try:
        k = int(input())
        head, tail = input().split("-", 1)

        tail = tail.replace("-", "")
        temp = ""
        for index in range(0, len(tail), k):
            line = tail[index: index + k]
            count1 = 0
            count2 = 0
            for c in line:
                if "A" <= c <= "Z":
                    count1 += 1
                if "a" <= c <= "z":
                    count2 += 1
            if count1 == count2:
                temp += line
            elif count1 > count2:
                temp += line.upper()
            else:
                temp += line.lower()

            # 按长度k分隔处理后的字符串
        dp = []
        for index in range(0, len(temp), k):
            dp.append(temp[index: index + k])

        print(f"{head}-{'-'.join(dp)}")

        # 推导式写法
        # print(f"{head}-{'-'.join([temp[index: index+k] for index in range(0, len(temp), k)])}")
    except Exception as e:
        break