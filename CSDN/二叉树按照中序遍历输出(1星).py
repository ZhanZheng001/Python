'''
题目描述
根据给定的二叉树结构描述字符串，输出该二叉树按照中序遍历结果字符串。中序遍历顺序为:左子树，根结点，右子树。

输入描述：
由大小写字母、左右大括号、逗号组成的字符串:

字母代表一个节点值，左右括号内包含该节点的子节点。
左右子节点使用逗号分隔，逗号前为空则表示左子节点为空,没有逗号则表示右子节点
为空。
二叉树节点数最大不超过100。
注:输入字符串格式是正确的，无需考虑格式错误的情况。
输出描述：
输出一个字符串，为二叉树中序遍历各节点值的拼接结果。

示例 1
输入：a{b{d, e{g,h{,I}}},c{f}}
输出：dbgehiafc
dbgehiafc
'''
# 先构造树，再中序输出，输入：a{b{d, e{g,h{,I}}},c{f}}
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_node(c):
    if type(c) == Node:
        return c
    elif c:
        return Node(c)
    else:
        return None


def get_root(stack):
    j = len(stack) - 1
    while j >= 0:
        if stack[j] == "{":
            break
        j -= 1

    if stack[j:][1] == ",":
        left_ = None
    else:
        left_ = get_node(stack[j:][1])

    if stack[j:][-1] == "," or "," not in stack[j:]:
        right_ = None
    else:
        right_ = get_node(stack[j:][-1])

    stack = stack[:j]
    root_ = get_node(stack.pop(-1))
    root_.left = left_
    root_.right = right_
    stack.append(root_)
    return stack


while 1:
    try:
        chars = input().replace(" ", "")

        # 构建树
        stack = []
        for c in chars:
            if c == "}":
                stack = get_root(stack)
            else:
                stack.append(c)

        dp = []

        # 中序输出
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dp.append(root.val)
            dfs(root.right)

        dfs(stack[0])
        print("".join(dp))
    except Exception as e:
        break
