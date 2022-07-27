'''
题目描述
二叉树也可以用数组来存储，给定一个数组，树的根节点的值储存在下标1，对于储存在下标n的节点，他的左子节点和右子节点分别储存在下标2n和2n+1，并且我们用-1代表一个节点为空，给定一个数组存储的二叉树，试求从根节点到最小的叶子节点的路径，路径由节点的值组成。

输入描述：
输入一行为数组的内容，数组的每个元素都是正整数，元素间用空格分割，注意第一个元素即为根节点的值，即数组的第n元素对应下标n，下标0在树的表示中没有使用，所以我们省略了，输入的树最多为7层。

输出描述：
输出从根节点到最小叶子节点的路径上各个节点的值，由空格分割，用例保证最小叶子节点只有一个。

示例 1
输入：3 5 7 -1 -1 2 4
输出：3 7 2

示例 2
输入：5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6
输出：5 8 7 6


'''
# 参考代码
# 定义树节点类；
# 根据输入构造二叉树；
# 遍历数，获取所有根节点到叶子节点路径；
# 根据叶子节点从小到大排序；
# 输出最小叶子节点路径。

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


while 1:
    try:
        nums = list(map(int, input().split()))

        # 构造二叉树
        root = Node(nums[0])
        stack = [root]
        i = 1
        while i < len(nums):
            r = stack[0]
            stack = stack[1:]

            r.left = Node(nums[i])
            stack.append(r.left)
            if i+1 < len(nums):
                r.right = Node(nums[i+1])
                stack.append(r.right)

            i += 2

        # 遍历数，获取路径
        dp = []

        def dfs(r, datas):
            if not r or r.data == -1:
                dp.append(datas)
                return

            dfs(r.left, datas+[r.data])
            dfs(r.right, datas+[r.data])

        dfs(root, [])
        # 根据叶子节点从小到大排序
        dp = sorted(dp, key=lambda x: x[-1])

        print(" ".join(map(str, dp[0])))
    except Exception as e:
        break