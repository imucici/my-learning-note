# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            
            if head.val == head.next.val:
                curp = head
                cur = head.next
                while cur != None and cur.val == curp.val:
                    cur = cur.next
                head = cur
                return Solution().deleteDuplicates(head)
            else:
                curp = head
                cur = head.next
                while cur.next != None and cur.val != cur.next.val:
                    curp = cur
                    cur = cur.next
                if cur.next == None:
                    return head
                else:
                    while cur.next != None and cur.val == cur.next.val:
                        cur = cur.next
                    curp.next = cur.next
                    return Solution().deleteDuplicates(head)
        
