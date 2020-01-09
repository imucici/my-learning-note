# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = []
        cur = head
        while cur != None:
            temp.append(cur.val)
            cur = cur.next
        p = temp[::-1]
        if p == temp:
            return True
        else:
            return False
