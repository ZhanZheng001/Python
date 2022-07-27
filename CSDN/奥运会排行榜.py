'''
题目描述
2012 伦敦奥运会即将到来，大家都非常关注奖牌榜的情况，现在我们假设奖牌榜的排名规则如下：
1、首先 gold medal 数量多的排在前面；
2、其次 silver medal 数量多的排在前面；
3、然后 bronzemedal 数量多的排在前面；
4、若以上三个条件仍无法区分名次，则以国家名称的字典序排定。

我们假设国家名称不超过 20 个字符、各种奖牌数不超过 100，且大于等于 0。

输入描述：
第一行输入一个整数 N(0<N<21)，代表国家数量;然后接下来的 N 行，每行包含一个字符串 Namei 表示每个国家的名称，和三个整数 Gi、 Si、 Bi 表示每个获得的 gold medal、
silver medal、 bronze medal 的数量，以空格隔开，如(China 51 20 21)，具体见样例输入。

输出描述：
输出奖牌榜的依次顺序，只输出国家名称，各占一行，具体见样例输出。

示例 1：
输入：
输出： China American Japan

示例 1
输入：

3
China 51 20 21
American 50 1 1
Japan 0 0 0
1
2
3
4
输出：

China
American
Japan
1
2
3
参考代码

'''
while 1:
    try:
        n = int(input())

        nums = [input().split() for _ in range(n)]

        print(nums)
        nums = sorted(
            nums,
            key=lambda x: (int(x[1]), int(x[2]), int(x[3]), x[0]),
            reverse=True
        )

        for i in nums:
            print(i[0])
    except Exception as e:
        break