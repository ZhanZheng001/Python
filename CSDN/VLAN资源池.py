'''
题目描述
Vlan是一种为局域网设备进行逻辑划分的技术，为了标识不同的vlan 引入了vlan id 1~4094之间的整数

定义一个vlan id 的资源池，资源池中连续的vlan用开始vlan-结束vlan表示，不连续的用单个整数表示，所有的vlan用英文逗号连接起来

现有一个vlan资源池，业务需要从资源池中申请一个vlan，需要你输出从vlan资源池中移除申请的vlan后的资源池

输入描述：
第一行为字符串格式的vlan资源池
第二行为业务要申请的vlan vlan的取值范围1~4094

输入池中vlan数量范围为2~2094的整数
资源池中vlan不重复且合法1~2094的整数
输入是乱序的

输出描述：
从输入vlan资源池中移除申请的vlan后，字符串格式的vlan资源池
输出要求满足题目中要求的格式，并且要求从小到大升序输出
如果申请的vlan不在原资源池，输出升序排序的原资源池的字符串即可

示例 1
输入：
1-5
2

输出：
1,3-5

说明：原vlan资源池中有1 2 3 4 5 移除2后
剩下的1 3 4 5按照升序排列的方式为 1 3-5

示例 2
输入：
20-21,15,18,30,5-10
15

输出：
5-10,18,20-21,30

说明：
原vlan资源池中有5 6 7 8 9 10 15 18 20 21 30
移除15后 剩下的为 5 6 7 8 9 10 18 20 21 30
按照题目描述格式并升序后的结果为5-10,18,20-21,30

示例 3
输入：
5,1-3
10

输出：
1-3,5

资源池中有1 2 3 5
申请的资源不在资源池中
将原池升序输出为1-3,5
'''
while 1:
    try:
        nums = input().split(",")
        vid = int(input())

        vlans = []
        for p in nums:
            val = p.split("-")
            if len(val) == 1:
                s = e = val[0]
            else:
                s, e = val
            vlans += list(range(int(s), int(e)+1))

        if vid in vlans:
            vlans.remove(vid)

        vlans = sorted(vlans)

        ret = []
        t = [vlans[0]]
        for vid in vlans[1:]:
            if t[-1] + 1 == vid:
                if len(t) < 2:
                    t.append(vid)
                else:
                    t[-1] = vid
            else:
                ret.append("-".join(map(str, t)))
                t = [vid]
        if t:
            ret.append("-".join(map(str, t)))

        print(",".join(ret))
    except Exception as e:
        break
