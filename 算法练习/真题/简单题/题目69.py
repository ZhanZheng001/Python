'''
        游戏规则：输入一个只包含英文字母的字符串，
        字符串中的俩个字母如果相邻且相同，就可以消除。
        在字符串上反复执行消除的动作，
        直到无法继续消除为止，
        此时游戏结束。
        输出最终得到的字符串长度。

        输出：原始字符串str只能包含大小写英文字母，字母的大小写敏感，长度不超过100，
        输出游戏结束后字符串的长度

        备注：输入中包含非大小写英文字母是均为异常输入，直接返回0。

        事例：mMbccbc输出为3
'''
while True:
    try:
        str1 = 'mMbccbc'
        list1 = list(str1)
        i = 0
        while i < len(list1)-1:
            if list1[i] == list1[i+1]:
                list1.remove(list1[i])
                list1.remove(list1[i])
                i -= 1
            else:
                i+=1
        print(len(list1)) if str1.isalpha() else print(0)
        break
    except:
        break
