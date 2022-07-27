'''
    定义当一个字符串只有元音字母(a,e,i,o,u,A,E,I,O,U)组成,
    称为元音字符串，现给定一个字符串，请找出其中最长的元音字符串，
    并返回其长度，如果找不到请返回0，
    字符串中任意一个连续字符组成的子序列称为该字符串的子串

    输入描述：
      一个字符串其长度 0<length ,字符串仅由字符a-z或A-Z组成
    输出描述：
      一个整数，表示最长的元音字符子串的长度

    示例1：
      输入
        asdbuiodevauufgh
      输出
        3
      说明：
        最长的元音字符子串为uio和auu长度都为3，因此输出3
'''
def isYuanyin(x):
    yuanyin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in x:
        if i not in yuanyin:
            return False
    return True

while True:
    try:
        str1 = 'asdbuiodevauufgh'.strip()
        tmp = []
        for i in range(len(str1)-1):
            for j in range(i+1,len(str1)+1):
                if isYuanyin(str1[i:j]):
                    tmp.append(len(str1[i:j]))
        print(max(tmp)) if tmp else print(0)
        break
    except:
        break
