'''
        一辆运送快递的货车。运送的快递均放在大小不等的长方形快递盒中
        为了能够装载更多的快递 同时不能让货车超载
        需要计算最多能装多少个快递
        快递的体积不受限制
        快递数量最多1000个
        货车载重量50000

        输入描述：
        第一行输入 每个快递重量 用逗号分隔
        如5,10,2,11
        第二行 输入 货车的载重量
        如20
        不需要考虑异常输入

        输出描述：
        输出最多能装多少个快递

        货车的载重量为20 最多只能放3种快递 5,10,2因此输出3

        示例1：
         输入
         5,10,2,11
         20
         输出
         3
'''
while True:
    try:
        list1 = list(map(int,'5,10,2,11'.strip().split(',')))
        max1 = int("20")
        list1.sort()#[2, 5, 10, 11] 20
        tmp = 0
        count = 0
        for i in range(len(list1)):
            tmp += list1[i]
            if tmp > max1:
                break
            else:
                count += 1
                continue
        print(count)
        break
    except:
        break