'''
给定一个随机的整数数组(可能存在正整数和负整数)nums,请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为最小值
并返回这两个数(按从小到大返回)以及绝对值。每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
输入描述：
 一个通过空格空格分割的有序整数序列字符串，最多1000个整数，
 且整数数值范围是[-65535,65535]
输出描述：
  两个数和两数之和绝对值
 示例一：
  输入
  -1 -3 7 5 11 15
  输出
  -3 5 2
说明：
因为|nums[0]+nums[2]|=|-3+5|=2最小，
所以返回-3 5 2
'''
while True:
    try:
        nums = list(map(int,'-1 -3 7 5 11 15'.strip().split()))#[-1, -3, 7, 5, 11, 15]
        min1 = abs(nums[0]+nums[1])
        list1 = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i] + nums[j]) < min1:
                    min1 = abs(nums[i] + nums[j])
                    list1 = [nums[i],nums[j]]
        list1 = list(map(str,sorted(list1)))
        print(' '.join(list1),min1)

        break
    except:
        break