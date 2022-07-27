'''
题目描述
有一个数列A[n]，从A[0]开始每一项都是一个数字，数列中A[n+1]都是A[n]的描述
其中A[0]=1

规则如下：
A[0]:1
A[1]:11 含义其中A[0]=1是1个1 即11
表示A[0]从左到右连续出现了1次1
A[2]:21 含义其中A[1]=11是2个1 即21
表示A[1]从左到右连续出现了2次1
A[3]:1211 含义其中A[2]从左到右是由一个2和一个1组成 即1211
表示A[2]从左到右连续出现了一次2又连续出现了一次1
A[4]:111221 含义A[3]=1211 从左到右是由一个1和一个2两个1 即111221
表示A[3]从左到右连续出现了一次1又连续出现了一次2又连续出现了2次1

输出第n项的结果
0<= n <=59

输入描述：
数列第n项 0<= n <=59

输出描述：
数列内容

示例 1
输入：4
输出：111221
'''
while 1:
    try:
        n = int("2")
        if n == 0:
            print("1")
        else:
            dp = [(1, "1")]
            for i in range(1, n):
                temp = ""
                for count, v in dp:
                    temp += f"{count}{v}"
                dp = []
                t = [temp[0]]
                for c in temp[1:]:
                    if t[-1] == c:
                        t.append(c)
                    else:
                        dp.append((len(t), t[0]))
                        t = [c]
                if t:
                    dp.append((len(t), t[0]))
            temp = ""
            for count, v in dp:
                temp += f"{count}{v}"
            print(temp)
            break
    except Exception as e:
        break
