'''
题目描述
输入形如 AB-ABC-cABd-Cb@ 的字符串，输入待分隔长度k； 要求输出保留第一个“-”前面的字符串格式，后面的每k个字符一分格，每三个字符中，大写字母数多的三个字母转大写，小写字母数多的三个字母转小写，一样多的不处理。

示例1：
输入:
AB-ABC-cABd-Cb@
2
1
2
输出:
AB-AB-CC-AB-dc-b@
1
说明：
AB- 保留
ABCcABdCb@ 每三个字符一组判断大小写
ABC -> ABC
cAB -> CAB
dCb -> dcb
@ -> @
转换后的再按长度 k 分隔
参考代码

'''
while 1:
    try:
        head, tail = input().split("-", 1)
        k = int(input())

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