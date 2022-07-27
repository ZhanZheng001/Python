'''
题目描述
特殊符号代替普通的计算方式比如 x#y = 2*x+y，x$y = x+3y， #优先级高于$。
比如输入 5#2$6 输出结果就是 30，因为先算 5#2 = 12，再算 12$6=30

示例 1
输入：5#2$6
输出：30

参考代码

'''
while 1:
    try:
        nums = input()

        stack = []
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == "#":
                stack.append(int("".join(nums[i:j])))
                stack.append(nums[j])
                i = j + 1
            elif nums[j] == "$":
                stack.append(int("".join(nums[i:j])))
                stack.append(nums[j])
                i = j + 1
            j += 1
        else:
            stack.append(int("".join(nums[i:j])))

        while "#" in stack:
            i = stack.index("#")
            stack[i-1] = 2 * stack[i-1]
            stack.pop(i)

        while "$" in stack:
            i = stack.index("$")
            stack[i+1] = 3 * stack[i+1]
            stack.pop(i)

        print(sum(stack))
    except Exception as e:
        break