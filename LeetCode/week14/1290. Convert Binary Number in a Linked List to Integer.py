# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = []
        while head != None:
            a.append(str(head.val))
            head = head.next
        a = "".join(a)
        a = int(a, 2)
        return a
