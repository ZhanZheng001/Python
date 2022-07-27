'''
题目描述
实现一个程序 search_matrix(matrix),参数 matrix 是一个仅包含 0 或 1 两种数字的矩阵,程序应返回输入矩阵中包含的最大正方形子矩阵(长和宽相等)的区域面积。

例如:如果 matrix 是[“1010111111”,“000000011”,“1010110111”,“0000110001”,那么它看起来像下面的阵:

1 0 1 0 1 1 1 1 1 1
0 0 0 0 0 0 0 1 1 1
1 0 1 0 1 1 0 1 1 1
0 0 0 0 1 1 0 0 0 1
1
2
3
4
对于上面的输入,最大的子矩阵是一个 3x3 的矩阵,程序只要返回最大子矩阵的面积即可,如上面的矩阵即返回 9(3x3)。

第 1 行输入为一个数字 N,代表下面有几行
第 2 行到第 N+1 行是代表矩阵的 0 和 1 组成的字符串,每行的长度相同

返回一个数字,代表输入矩阵的最大正方子矩阵的面积。

示例 1
输入：

3
1 1 0
1 1 1
1 1 0
1
2
3
4
输出：

6
1
参考代码

'''
def dfs(heights):
    stack = [(-1, -1)]
    H = heights + [0]
    ans = 0
    for i, h in enumerate(H):
        while stack[-1][1] > h:
            _, oh = stack.pop()
            s = (i - stack[-1][0] - 1) * oh
            ans = max(ans, s)
        stack.append((i, h))
    return ans


while 1:
    try:
        matrix = [input().split() for _ in range(int(input()))]
        if not matrix:
            print(0)
            break

        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if matrix[i][j] == '0' else dp[j] + 1
            ans = max(ans, dfs(dp))

        print(ans)
    except Exception as e:
        break