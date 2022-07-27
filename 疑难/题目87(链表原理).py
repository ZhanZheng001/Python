# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
#
#  如果有两个中间结点，则返回第二个中间结点。
#
#
#
#  示例 1：
#
#
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next =
# NULL.
#
#
#  示例 2：
#
#
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
#
#
#
#
#  提示：
#
#
#  给定链表的结点数介于 1 和 100 之间。
#
#  Related Topics 链表 双指针 👍 562 👎 0

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
# leetcode submit region end(Prohibit modification and deletion)
def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head

def print_linked_list(list_node):
    if list_node is None:
        return

    cur = list_node
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('null')

if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.middleNode(head)
    print('结果：')
    print_linked_list(result)

