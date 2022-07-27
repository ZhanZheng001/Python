'''
题目描述
九宫格按键输入，判断输出，有英文和数字两个模式，默认是数字模式，数字模式直接输出数字，英文模式连续按同一个按键会
依次出现这个按键上的字母，如果输入”/”或者其他字符，则循环中断。
要求输入一串按键，输出屏幕显示。

输入描述：
输入范围为数字 0~9 和字符’#’、’/’，输出屏幕显示，例如，
在数字模式下，输入 1234，显示 1234
在英文模式下，输入 1234，显示,adg
输出描述：
#用于切换模式，默认是数字模式，执行#后切换为英文模式；
/表示延迟，例如在英文模式下，输入 22/222，显示为 bc；
英文模式下，多次按同一键，例如输入 22222，显示为 b；

示例 1
输入输出示例仅供调试，后台判题数据一般不包含示例
输入
123#222235/56
输出
123adjjm
'''
def f(x):
    dic = {'1': ',.', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    num_mode = True
    length = len(x)
    i = 0
    result = ""
    while i < length:
        s: str = x[i]
        if s == '#':
            num_mode = not num_mode
            i += 1
            continue
        if s == '/':
            i += 1
            continue
        if num_mode:
            result += s
            i += 1
            continue
        if s == '0':
            result += " "
            i += 1
            continue
        cnt = 0
        while i < length and x[i] == s:
            cnt += 1
            i += 1
        string = dic[s]
        result += string[cnt % len(string) - 1]
    return result
while True:
    try:
        line = str("123#222235/56".strip())
        results = f(line)
        print(results)
        break
    except:
        break


