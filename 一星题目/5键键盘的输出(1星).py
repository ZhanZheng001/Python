'''
题目描述
有一个特殊的5键键盘，上面有a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键。
a键在屏幕上输出一个字母a；
ctrl-c将当前选择的字母复制到剪贴板；
ctrl-x将当前选择的字母复制到剪贴板，并清空选择的字母；
ctrl-v将当前剪贴板里的字母输出到屏幕；
ctrl-a选择当前屏幕上的所有字母。

注意：
剪贴板初始为空，新的内容被复制到剪贴板时会覆盖原来的内容
当屏幕上没有字母时，ctrl-a无效
当没有选择字母时，ctrl-c和ctrl-x无效
当有字母被选择时，a和ctrl-v这两个有输出功能的键会先清空选择的字母，再进行输出
给定一系列键盘输入，输出最终屏幕上字母的数量。

输入描述:
输入为一行，为简化解析，用数字1 2 3 4 5代表a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键的输入，数字用空格分隔
输出描述:
输出一个数字，为最终屏幕上字母的数量

示例 1
输入：
1 1 1
输出：
3
说明
连续键入3个a，故屏幕上字母的长度为3

示例 2
输入：
1 1 5 1 5 2 4 4
输出：
2
说明
输入两个a后ctrl-a选择这两个a，再输入a时选择的两个a先被清空，所以此时屏幕只有一个a，后续的ctrl-a，ctrl-c选择并复制了这一个a，最后两个ctrl-v在屏幕上输出两个a，故屏幕上字母的长度为2（第一个ctrl-v清空了屏幕上的那个a）
'''
while 1:
    try:
        nums = '1 1 5 1 5 2 4 4'.split()
        dp = "" # 屏幕输出
        slt = "" # 选择区
        cache = "" # 粘贴板
        for c in nums:
            if c == '1':# a键在屏幕上输出一个字母a
                if slt:
                    dp = "a"
                    slt = ""
                else:
                    dp += "a"
            elif c == '2':# ctrl - c将当前选择的字母复制到剪贴板
                if slt:
                    cache = slt
            elif c == '3':# ctrl - x将当前选择的字母复制到剪贴板，并清空选择的字母
                if slt:
                    cache = slt
                    slt = ""
                    dp = ""
            elif c == '4':# ctrl - v将当前剪贴板里的字母输出到屏幕
                if cache:
                    if slt:
                        dp = cache
                        slt = ""
                    else:
                        dp += cache
            else:# ctrl - a选择当前屏幕上的所有字母
                if dp:
                    slt = dp
        print(len(dp))
        break
    except Exception as e:
        break
