'''
题目描述
存在一种虚拟IPv4地址，由4小节组成，每节的范围为0~128，以#号间隔，格式如下：
(1-128)#(0-255)#(0-255)#(0-255)
请利用这个特性把虚拟IPv4地址转换为一个32位的整数，IPv4地址以字符串形式给出，要求每个IPvV4地址只能对应到唯一的整数上。
如果是非法IPv4，返回invalid IP。

输入描述：
输入一行，虚拟IPv4地址格式字符串
输出描述：
输出一行，按照要求输出整型或者特定字符

示例 1
输入：
100#101#1#5
输出：
1684340997

示例 2
输入：
1#2#3
输出：
invalid IP
'''
while 1:
    try:
        nums = list(map(int, '100#101#1#5'.split("#"))) #不能有其他符合,不能#号结尾
        if len(nums) != 4:
            print("invalid IP")
            break
        else:
            dp = ""
            for i in range(4):
                if not ((i == 0 and 1 <= nums[i] <= 128) or (i > 0 and 0 <= nums[i] <= 255)):
                    print("invalid IP")
                    break
                dp += bin(nums[i])[2:].zfill(8)
            print(int(dp, 2))
            break
    except Exception as e:
        break