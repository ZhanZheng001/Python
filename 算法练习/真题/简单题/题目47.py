'''
         相对开音节构成的结构为辅音+元音(aeiou)+辅音(r除外)+e
         常见的单词有bike cake
         给定一个字符串，以空格为分隔符
         反转每个单词的字母
         若单词中包含如数字等其他非字母时不进行反转
         反转后计算其中含有相对开音节结构的子串个数
         (连续子串中部分字符可以重复)

         输入描述
            字符串 以空格分割的多个单词
            长度<10000 字母只考虑小写

         输出描述
             含有相对开音节结构的子串个数

         示例1：
            输入
              ekam a ekac
            输出
              2
            说明：
             反转后为  make a cake 其中make和cake为相对开音节子串
             返回2

          示例2：
             输入
                !ekam a ekekac
             输出
                 2
             说明
                 反转后为 !ekam a cakeke
                 因为!ekam含有非英文字母，所以未反转
                 其中 cake和keke 为相对开音节子串 返回2
'''
def fan(x):
    for i in range(len(x)):
        if x[i].isalpha():
            x[i] = x[i][::-1]
            continue
        else:
            continue
    return x
def isYuan(x):
    if len(x) < 4:
        tmp = 0
    else:
        tmp = 0
        for i in range(len(x)-3):
            if x[i].islower() and x[i] not in 'aeiou' :
                if x[i+1].islower() and x[i+1] in 'aeiou':
                    if x[i+2].islower() and x[i+2] not in 'aeiour':
                        if x[i+3] =='e':
                            tmp += 1
                        else:continue
                    else:continue
                else:continue
            else:continue
    return tmp

while True:
    try:
        list1 = '!ekam a ekekac'.strip().split()   #['ekam', 'a', 'ekac']
        fan(list1)  #['make', 'a', 'cake']
        res = 0
        for i in range(len(list1)):
            res += isYuan(list1[i])
        print(res)
        break
    except:
        break