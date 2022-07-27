'''
题目描述
近些年来，我国防沙治沙取得显著成果。某沙漠新种植N棵胡杨（编号1-N），排成一排。
一个月后，有M棵胡杨未能成活。
现可补种胡杨K棵，请问如何补种（只能补种，不能新种），可以得到最多的连续胡杨树？

输入描述：
N 总种植数量
M 未成活胡杨数量
M 个空格分隔的数，按编号从小到大排列
K 最多可以补种的数量
其中：
1 <= N <= 100000
1 <= M <= N
0 <= K <= M
输出描述：
最多的连续胡杨棵树
示例 1
输入：
5
2
2 4
1
输出：
3
说明：
补种到2或4结果一样，最多的连续胡杨棵树都是3。
'''
while 1:
    try:
        n = int("5")
        m = int("2")
        nums = list(map(int, "2 4".split()))
        k = int("1")
        nums = [0 if i + 1 in nums else 1 for i in range(n)] #[1, 0, 1, 0, 1]
        max_ = 0
        i = 0
        j = min(k, n) #可补种数量大于总数时,上限取总数n
        while j < len(nums):
            count = nums[i:j].count(0)  #多少个0即代表补种了多少颗
            if count < k: #补种数量小于k时,继续补种,右指针右移
                j += 1
            elif count == k: #补种数量等于k时,返回最大连续数量
                max_ = max([j-i, max_])
                j += 1
            else: #补种的数量超过k时,左指针右移,直到遍历完
                i += 1
        else:
            max_ = max([j - i, max_])
        print(max_)
        break
    except Exception as e:
        break
