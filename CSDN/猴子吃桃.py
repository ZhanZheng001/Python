'''
题目描述
孙悟空喜欢吃蟠桃，一天他乘守卫蟠桃园的天兵天将离开了而偷偷的来到王母娘娘的蟠桃园偷吃蟠桃。

已知蟠桃园有 N 棵蟠桃树，第 i 棵蟠桃树上有 N[i]（大于 0）个蟠桃，天兵天将将在 H（不小于蟠桃树棵数）小时后回来。

孙悟空可以决定他吃蟠桃的速度 K（单位：个/小时），每个小时他会选则一颗蟠桃树，从中吃掉 K 个蟠桃，如果这棵树上的蟠桃数小于 K，他将吃掉这棵树上所有蟠桃，然后这一小时内不再吃其余蟠桃树上的蟠桃。孙悟空喜欢慢慢吃，但仍想在天兵天将回来前将所有蟠桃吃完。

求孙悟空可以在 H 小时内吃掉所有蟠桃的最小速度 K（K 为整数）。

输入描述：
从标准输入中读取一行数字，前面数字表示每棵数上蟠桃个数，最后的数字表示天兵天将将离开的时间。

输出描述：
吃掉所有蟠桃的最小速度 K（K 为整数）或输入异常时输出-1。

示例 1
输入：
3 11 6 7 8
输出：
4

参考代码
树的个数大于h时，已最大速度吃也吃不完，输出-1
最大速度是 一个树上的最大个数，可以从1 - max 分别计算，满足 sum(nums[i]/k) <= H，就是最小速度


'''
while 1:
    try:
        *nums, h = list(map(int, input().split()))

        if len(nums) > h:
            print(-1)
        else:
            for i in range(1, max(nums)+1):
                if sum([int(n/i+0.5) for n in nums]) <= h:
                    print(i)
                    break
            else:
                print(-1)

    except Exception as e:
        break