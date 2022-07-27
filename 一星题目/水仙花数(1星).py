'''
题目描述
【水仙花数】
给定非空字符串s，将该字符串分割成一些子串，使每个子串的ASCII码值的和均为水仙花数。
若分割不成功，则返回0；
若分割成功且分割结果不唯一，则返回-1；
若分割成功且分割结果唯一，则返回分割后子串的数目。

输入描述：
输入字符串的最大长度为200
输出描述：
根据题目描述中情况，返回相应的结果。
示例 1
输入：
abc
输出：
0
说明：
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
'''
def fun(num):
    a, b, c = list(map(int, list(str(num))))
    return a**3 + b**3 + c**3 == num
while 1:
    try:
        base = "abc"
        nums = [ord(c) for c in base] #[97, 98, 99]
        i,j = 0,1
        dp = []
        def dfs(inums, subs):
            i,j = 0,1
            while j <= len(inums):
                total = sum(inums[i: j])
                if total < 100:
                    j += 1
                elif total < 1000:
                    if fun(total):
                        dfs(inums[j:], subs+["".join([chr(n) for n in inums[i: j]])])
                    j += 1
                else:
                    break
            else:
                if "".join(subs) == base:
                    dp.append(subs)
        dfs(nums, [])
        if not dp:
            print(0)
        elif len(dp) == 1:
            print(len(dp[0]))
        else:
            print(-1)
        break
    except Exception as e:
        break