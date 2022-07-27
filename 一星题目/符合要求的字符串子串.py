'''
给定两个字符串,从字符串2中找出字符串1中的所有字符,去重并按照ASCII码值从小到大排列;
输入字符串1长度不超过1024;字符串2长度不超过1000000
字符范围满足ASCII编码要求，按照ASCII由小到大排序
示例1:
输入
    bach
    bbaaccddfg
输出
    abc
示例2:
输入
    fach
    bbaaccedfg
输出
    acf
'''
while True:
    try:
        list1 = sorted(list(set("fach".strip())))
        str2 = "bbaaccedfg".strip()
        tmp = []
        for char in list1:
            if char in str2:
                tmp.append(char)
        print("".join(tmp)) if tmp else print("-1")
        break
    except:
        break