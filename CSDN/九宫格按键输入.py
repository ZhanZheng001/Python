'''
题目描述
九宫格按键输入，判断输出，有英文和数字两个模式，默认是数字模式，数字模式直接输出数字，英文模式连续按同一个按键会依次出现这个按键上的字母，如果输入"/"或者其他字符，则循环中断

1（,.） 2（abc） 3（def）
4（ghi） 5（jkl） 6（mno）
7（pqrs） 8（tuv） 9（wxyz）
#0（空格） /

要求输入一串按键，输出屏幕显示

输入描述：
输入范围为数字 0~9 和字符’#'、 ’/’，输出屏幕显示，例如，
在数字模式下，输入 1234，显示 1234
在英文模式下，输入 1234，显示,adg

输出描述：
1、 #用于切换模式，默认是数字模式，执行#后切换为英文模式；
2、 /表示延迟，例如在英文模式下，输入 22/222，显示为 bc；
3、英文模式下，多次按同一键，例如输入 22222，显示为 b；

示例 1
输入： 123#222235/56
输出： 123adjjm

参考代码

'''
dct = {
    "1": ',.',
    "2": 'abc',
    "3": 'def',
    "4": 'ghi',
    "5": 'jkl',
    "6": 'mno',
    "7": 'pqrs',
    "8": 'tuv',
    "9": 'wxyz',
}


def func(nums):
    if nums and nums[0] in dct:
        que = dct[nums[0]]
        return que[len(nums) % len(que)-1]
    else:
        return nums


while 1:
    try:
        nums = input()

        # True 数字
        # False 拼音
        flg = True

        ret = ""
        bef = ""
        for c in nums:
            if c == "#":
                flg = not flg
                ret += func(bef)
                bef = ""
            elif flg:
                ret += func(bef)
                bef = ""
                ret += c
            else:
                if c == "/":
                    ret += func(bef)
                    bef = ""
                elif bef and c == bef[-1]:
                    bef += c
                else:
                    ret += func(bef)
                    bef = c
        if bef:
            ret += func(bef)

        print(ret)
    except Exception as e:
        break