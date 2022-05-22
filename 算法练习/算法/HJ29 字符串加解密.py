'''
描述
1、对输入的字符串进行加解密，并输出。
2、加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。

本题含有多组样例输入。
输入描述：
输入说明
输入一串要加密的密码
输入一串加过密的密码

输出描述：
输出说明
输出加密后的字符
输出解密后的字符

示例1
输入：
abcdefg
BCDEFGH
复制
输出：
BCDEFGH
abcdefg
'''
while True:
    try:
        input_str = input()
        input_passwd = input()
        output_passwd = ''
        output_str = ''
        for ch in input_str:
            if ch.isupper():
                output_passwd += 'a' if ch == 'Z' else chr(ord(ch) + 1).lower()
            elif ch.islower():
                output_passwd += 'A' if ch == 'z' else chr(ord(ch) + 1).upper()
            elif ch.isnumeric():
                output_passwd += '0' if ch == '9' else str(int(ch) + 1)
            else:
                output_passwd += ch
        print(output_passwd)
        for pa in input_passwd:
            if pa.isupper():
                output_str += 'z' if pa == 'A' else chr(ord(pa) - 1).lower()
            elif pa.islower():
                output_str += 'Z' if pa == 'a' else chr(ord(pa) - 1).upper()
            elif pa.isnumeric():
                output_str += '9' if pa == '0' else str(int(pa)-1)
            else:
                output_str += pa
        print(output_str)
    except:
        break