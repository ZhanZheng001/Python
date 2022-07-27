'''
    /*
    删除字符串中出现次数最少的字符
    如果多个字符出现次数一样则都删除

    例子：
    输入
      abcdd
      字符串中只
     输出
      dd

    输入
      aabbccdd

    输出
      empty

      如果都被删除  则换为empty

     */
'''
while True:
    try:
        str1='abcdd'
        count_min=len(str1)
        for i in set(str1):
            if str1.count(i) < count_min:
                count_min = str1.count(i)
        tmp=[]
        for i in set(str1):
            if str1.count(i)==count_min:
                tmp.append(i)
        list1 =list(str1)
        for i in tmp:
            list1.remove(i)
        print(''.join(list1)) if list1 else print('empty')
        break
    except:
        break