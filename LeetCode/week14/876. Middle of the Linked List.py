# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def middleNode(self, head):
        size = 0
        cur = head
        while cur != None:
            cur = cur.next
            size+=1
            
        mid = size//2
        count = 0
        target = head
        while count != mid:
            target = target.next
            count+=1
        return target
