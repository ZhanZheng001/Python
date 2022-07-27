'''
在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符
注意：匹配时不区分大小写。
输入：
通配符表达式；
一组字符串。
输出：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
数据范围：字符串长度：1≤s≤100
进阶：时间复杂度：O(n^2) ，空间复杂度：O(n)
输入描述：
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串
输出描述：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false

示例1
输入：
te?t*.*
txt12.xls
输出：
false

示例2
输入：
?*Bc*?
abcd
输出：
true

示例3
输入：
h*?*a
h#a
输出：
false
说明：根据题目描述可知能被*和?匹配的字符仅由英文字母和数字0到9组成，所以?不能匹配#，故输出false

https://www.nowcoder.com/questionTerminal/43072d50a6eb44d2a6c816a283b02036?answerType=1&f=discussion
'''
import re
while True:
    try:
        str1 = input().strip().lower()
        str2 = input().strip().lower()
        str1 = str1.replace(".", "\.").replace("*", "[a-z0-9]*").replace("?", "[a-z0-9]{1}")
        #str1 = f"^{str1}$"  #不能用全匹配,容易超时. 建议用findall搜索快
        if str2 in re.findall(str1,str2):
            print("true")
        else:
            print("false")
    except:
        break