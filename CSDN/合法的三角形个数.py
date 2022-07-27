'''
题目描述
给一个长度为N的非负整数数组nums，请你计算一下，有多少个三元组代表的边长可以组成三角形。

数据范围:
1≤N≤1000
0≤nums[i]≤1000

示例1
输入：
2 3 4 4
1
输出：
4
1
说明：
合法的有4个：
2 3 4(第一个4)
2 3 4(第二个4)
2 4 4
3 4 4
示例2
输入：
4 2 3 4
1
输出：
4
1
'''
# 参考代码
# 方法一：
# 暴力解，简单好记，能通过92%
# while 1:
#     try:
#         nums = list(map(int, input().split()))
#         nums = sorted(nums)
#         lens = len(nums)
#         count = 0
#         for i in range(lens-2):
#             for j in range(i + 1, lens-1):
#                 for k in range(j + 1, lens):
#                     a = nums[i]
#                     b = nums[j]
#                     c = nums[k]
#                     # 任意两条边之和要大于第三边
#                     if a + b > c:
#                         count += 1
#         print(count)
#     except Exception:
#         break

# 方法二：
# 双指针（滑动窗口）

while 1:
    try:
        nums = list(map(int, input().split()))
        nums = sorted(nums)
        lens = len(nums)

        # [left, right] 窗口内的数和 [i] 始终满足三角形
        count = 0
        for i in range(lens):
            left = i + 1
            right = i + 2
            while left < lens:
                while right < lens and nums[right] < nums[i] + nums[left]:
                    count += max(right - left, 0)
                    right += 1
                left += 1
        print(count)
    except Exception:
        break