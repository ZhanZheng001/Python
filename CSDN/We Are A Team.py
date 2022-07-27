'''
题目描述
总共有 n 个人在机房，每个人有一个标号（1<=标号<=n），他们分成了多个团队，需要你根据收到的 m 条消息判定指定的两个人是否在一个团队中，具体的：
1、消息构成为 a b c，整数 a、b 分别代表两个人的标号，整数 c 代表指令
2、c == 0 代表 a 和 b 在一个团队内
3、c == 1 代表需要判定 a 和 b 的关系，如果 a 和 b 是一个团队，输出一行’we are a team’,如果不是，输出一行’we are not a team’
4、c 为其他值，或当前行 a 或 b 超出 1~n 的范围，输出‘da pian zi’

输入描述：
1、第一行包含两个整数 n，m(1<=n,m<100000),分别表示有 n 个人和 m 条消息
2、随后的 m 行，每行一条消息，消息格式为：a b c(1<=a,b<=n,0<=c<=1)

输出描述:
1、c ==1,根据 a 和 b 是否在一个团队中输出一行字符串，在一个团队中输出‘we are a team’,不在一个团队中输出’we are not a team’
2、c 为其他值，或当前行 a 或 b 的标号小于 1 或者大于 n 时，输出字符串‘da pian zi’
3、如果第一行 n 和 m 的值超出约定的范围时，输出字符串’Null’

示例 1
输入：

5 7
1 2 0
4 5 0
2 3 0
1 2 1
2 3 1
4 5 1
1 5 1
1
2
3
4
5
6
7
8
输出：

We are a team
We are a team
We are a team
We are not a team
1
2
3
4
示例 2
输入：

5 6
1 2 0
1 2 1
1 5 0
2 3 1
2 5 1
1 3 2
1
2
3
4
5
6
7
输出：

we are a team
we are not a team
we are a team
da pian zi
1
2
3
4
参考代码

'''
while 1:
    try:
        n, m = list(map(int, input().split()))

        nums = []
        for _ in range(m):
            tmp = input().split()
            a = int(tmp[0])
            b = int(tmp[1])
            com = tmp[2]
            nums.append((a, b, com))

        dp = []
        for a, b, com in nums:
            if not (1 <= a <= n and 1 <= b <= n):
                print("da pian zi")
                continue
            if com == "0":
                if dp:
                    for idx, val in enumerate(dp):
                        if val.intersection({a, b}):
                            dp[idx] = val.union({a, b})
                            break
                    else:
                        dp.append({a, b})
                else:
                    dp.append({a, b})
            elif com == "1":
                for i in dp:
                    if i.intersection({a, b}) == {a, b}:
                        print("we are a team")
                        break
                else:
                    print("we are not a team")
            else:
                print("da pian zi")
    except Exception as e:
        break