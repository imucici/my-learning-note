# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        
        elif head.val == val :
            head = head.next
            return Solution().removeElements(head,val)
    
        else:
            curp  = head
            cur = head.next
            while cur != None and cur.val != val :
                curp = cur
                cur = cur.next

            if cur == None:
                return head
            else:
                curp.next = cur.next
                return Solution().removeElements(head,val)

            
            
        
