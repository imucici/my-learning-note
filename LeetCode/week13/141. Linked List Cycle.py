# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return None
        else:
            lst = []
            cur = head
            while cur != None and cur not in lst:
                lst.append(cur)
                cur = cur.next
            return cur
