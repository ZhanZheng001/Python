'''
题目描述
TLV编码是按[Tag Length Value]格式进行编码的，一段码流中的信元用Tag标识，Tag在码流中唯一不重复，Length表示信元Value的长度，Value表示信元的值。
码流以某信元的Tag开头，Tag固定占一个字节，Length固定占两个字节，字节序为小端序。
现给定TLV格式编码的码流，以及需要解码的信元Tag，请输出该信元的Value。
输入码流的16机制字符中，不包括小写字母，且要求输出的16进制字符串中也不要包含小写字母；码流字符串的最大长度不超过50000个字节。

输入描述：
输入的第一行为一个字符串，表示待解码信元的Tag；
输入的第二行为一个字符串，表示待解码的16进制码流，字节之间用空格分隔。
输出描述：
输出一个字符串，表示待解码信元以16进制表示的Value。

示例1：
输入
31
32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC
输出：
32 33
'''

# 一个 key Value 的格式为 [Tlag Length Value]；
# Tlag 占一个字节 Length 占两个字节；
# Tlag=32， Length=01 00， Value=AE；
# Tlag=90， Length=02 00， Value=01 02；
# Tlag=30， Length=03 00， Value=AB 32 31；
# Tlag=31， Length=02 00， Value=32 33；
# Tlag=33， Length=01 00， Value=CC；
while 1:
    try:
        Tag = "31"
        nums = "32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC".split()
        dct = {}
        key = None
        lens = None
        while nums:
            if key:
                if lens:
                    dct[key] = nums[0:int(lens)]# 根据 整型信元长度 截取 Value
                    nums = nums[int(lens):]
                    key = None
                    lens = None
                else:
                    lens = int("".join(nums[0:2][::-1]))# 获取两字节信元长度
                    nums = nums[2:]
            else:
                key = nums[0]# 获取信元的Tag
                nums = nums[1:]
        # dct = {'32': ['AE'], '90': ['01', '02'], '30': ['AB', '32', '31'], '31': ['32', '33'], '33': ['CC']}
        print(" ".join(dct[Tag]))# 输出目标 信元 的 Value
        break
    except Exception as e:
        break
