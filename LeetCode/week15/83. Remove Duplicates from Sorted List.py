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
            curp = head
            cur = head.next
            if curp.val == cur.val: #一開始就有重複值
                while cur != None and cur.val == curp.val:
                    cur = cur.next
                curp.next = cur
                return Solution().deleteDuplicates(head)
            else:
                while cur.next != None and cur.val != cur.next.val:
                    curp = cur
                    cur = cur.next
                
                if cur.next == None:
                    return head
                else:
                    curp = cur
                    cur = cur.next
                    while cur != None and cur.val == curp.val:
                        cur = cur.next
                    curp.next = cur
                    return Solution().deleteDuplicates(head)
