'''
幼儿园两个班的小朋友在排队时混在了一起，每位小朋友都知道自己是否与前面一位小朋友同班，请你帮忙把同班的小朋友找出来。
小朋友的编号是整数，与前一位小朋友同班用Y表示，不同班用N表示。

输入描述：
输入为空格分开的小朋友编号和是否同班标志。
输出描述：
输出为两行，每一行记录一个班小朋友的编号，编号用空格分开，且：
1.编号需按照升序排列。
2.若只有一个班的小朋友，第二行为空行。

比如：
输入
1/N 2/Y 3/N 4/Y
输出
1 2
3 4
'''
# 参考代码
# 准备两个列表A和B, 分别保存两个班的学生
# 第一个输入的同学默认保存在A
# 后面的以此判断N Y 确定要保存的列表
while 1:
    try:
        nums = input().split()

        # 第一个同学
        start = nums[0].split('/')
        A = [start[0]]
        B = []

        temp = [A, B]  # 表示前一个同学的班级， 默认是 A 班级
        # 从第二个同学开始判断
        for n in nums[1:]:
            id_, f = n.split("/")

            if f == "Y":
                temp = temp
            else:
                temp = temp[::-1]

            temp[0].append(id_)

        if A:
            print("".join(A))
        if B:
            print("".join(B))
    except Exception as e:
        break
