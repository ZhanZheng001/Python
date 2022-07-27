'''
题目描述
树形目录，m行输入，[当前目录ID 父级目录ID]。最后一行为待删除目录ID，要求删除父级同时删除下级目录。 输出剩余目录。

示例1
输入：

6
3 1
5 1
4 3
10 5
11 5
12 4
5
1
2
3
4
5
6
7
8
解释：树的结构，删除 5 的同时需要删除 10， 11。

        1
       /  \
     3     5
    /     /  \
   4     10  11
  /
12
1
2
3
4
5
6
7
输出：

3 1
4 3
12 4
1
2
3
参考代码

'''
while 1:
    try:
        num = int(input())

        lst = []
        tree = {}
        for _ in range(num):
            child, parent = input().split()
            if parent in tree:
                tree[parent].append(child)
            else:
                tree[parent] = [child]
            lst.append((child, parent))


        def del_child(parent_id):
            if parent_id in tree:
                for child_id in tree.pop(parent_id):
                    lst.remove((child_id, parent_id))
                    del_child(child_id)


        del_id = input()
        del_child(del_id)

        for c in lst:
            if c[0] != del_id:
                print(" ".join(c))

    except Exception:
        break