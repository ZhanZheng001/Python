'''
题目描述
将电话号码 one two……nine zero
翻译成 1 2 ….9 0
中间会有 double
例如输入： OneTwoThree 输出： 123
输入： OneTwoDoubleTwo 输出： 1222
输入： 1Two2 输出： ERROR
输入： DoubleDoubleTwo 输出： ERROR
有空格，非法字符，两个 Double 相连， Double 位于最后一个单词都错误

示例 1
输入：onetwothreeonetwodoubletwo
输出：1231222


'''
# 参考代码
# 使用 replace 把单词处理成 对应的数字

dct = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "double": "#",
}

while 1:
    try:
        nums = input()

        for k, v in dct.items():
            nums = nums.replace(k, v)

        ret = []
        i = 0
        while i < len(nums):
            if "0" <= nums[i] <= "9":
                ret.append(nums[i])
            elif nums[i] == "#":
                if i + 1 < len(nums) and "0" <= nums[i+1] <= "9":
                    ret.append(nums[i+1])
                else:
                    print("error")
                    break
            else:
                print("error")
                break
            i += 1
        else:
            print("".join(ret))
    except Exception as e:
        break