while True:
    try:
        nums = list(map(int,'-3 -1 5 7 11 15'.strip().split())) #[-3, -1, 5, 7, 11, 15]
        min1 = abs(nums[0]+nums[1])
        list1 = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]+nums[j]) < min1:
                    min1 = abs(nums[i]+nums[j])
                    list1 = [nums[i]+nums[j]]
        print(min1)
        break
    except:
        break