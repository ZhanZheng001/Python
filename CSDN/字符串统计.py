'''
题目描述
给定两个字符集合，一个为全量字符集，一个为已占用字符集。已占用的字符集中的字符不能再使用，要求输出剩余可用字符集。

输入描述：
1、输入为一个字符串，一定包含@符号。 @前的为全量字符集， @后的字为已占用字符集。
2、已占用字符集中的字符一定是全量字符集中的字符。字符集中的字符跟字符之间使用英文逗号分隔。
3、每个字符都表示为字符加数字的形式，用英文冒号分隔，比如 a:1，表示 1 个 a 字符。
4、字符只考虑英文字母，区分大小写，数字只考虑正整形，数量不超过 100。
5、如果一个字符都没被占用， @标识仍然存在，例如 a:3,b:5,c:2@

输出描述：
输出可用字符集，不同的输出字符集之间回车换行。 注意，输出的字符顺序要跟输入一致。不能输出 b:3,a:2,c:2 如果某个字符已全被占用，不需要再输出。

示例 1
输入：

a:3,b:5,c:2@a:1,b:2
1
输出：

a:2,b:3,c:2
1
参考代码

'''
while 1:
    try:
        a, b = input().split("@")
        lst = [c.split(':') for c in a.split(',')]
        if not b:
            print(f"{a}@")
            break
        dct = {}

        for c in b.split(','):
            k, v = c.split(':')
            dct[k] = int(v)

        for item in lst:
            if item[0] in dct:
                count = int(item[1]) - dct[item[0]]
                if count > 0:
                    item[1] = str(count)
                else:
                    lst.remove(item)

        print(",".join([f"{i[0]}:{i[1]}" for i in lst]))
    except Exception as e:
        break