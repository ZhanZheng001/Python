'''
题目描述
将输入的字符串（字符串仅包含小写字母‘a’到‘z’），按照如下规则，循环转换后输出： a->b,b->c,…,y->z,z->a；若输入的字符串连续出现两个字母相同时，后一个字母需要连续转换 2 次。

例如： aa 转换为 bc， zz 转换为 ab；当连续相同字母超过两个时，第三个出现的字母按第一次出现算。

示例 1
输入：aa
输出：bc

示例 2
输入：aaa
输出：bcb

参考代码

'''
def func(c):
    if c == "z":
        return "a"
    else:
        return chr(ord(c)+1)


while 1:
    try:
        nums = input()

        dp = []
        ret = func(nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and i-1 not in dp:
                ret += func(func(nums[i]))
                dp.append(i)
            else:
                ret += func(nums[i])

        print(ret)
    except Exception as e:
        break