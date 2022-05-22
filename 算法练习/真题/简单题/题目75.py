'''
/*
  输入一串字符串
  字符串长度不超过100
  查找字符串中相同字符连续出现的最大次数

  输入描述
    输入只有一行，包含一个长度不超过100的字符串

  输出描述
    输出只有一行，输出相同字符串连续出现的最大次数

   说明：
     输出

   示例1：
     输入
       hello
     输出
       2

    示例2：
      输入
       word
      输出
       1

     示例3：
      输入
        aaabbc
       输出
        3

    字符串区分大小写
   */
'''

while True:
    try:
        str1 = 'aaabbc'.strip()
        list1 = []
        i,j = 0,0
        while j < len(str1):
            if str1[i] == str1[j]:
                j += 1
                if j == len(str1):
                    list1.append(len(str1[i:j]))
            else:
                list1.append(len(str1[i:j]))
                i = j
                if i == len(str1)-1:
                    list1.append(1)
                    break
                j += 1
        # print(list1)
        print(max(list1))
        break
    except:
        break
