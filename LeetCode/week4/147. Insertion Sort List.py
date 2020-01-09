# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            new = ListNode(head.val)
            compare = head.next
            curp = new
            cur = new.next

            while compare != None:
                if compare.val <= curp.val:
                    nnew = ListNode(compare.val)
                    nnew.next = new
                    new = nnew
                else:
                    nnew = ListNode(compare.val)
                    while cur != None and cur.val < nnew.val:
                        curp = cur
                        cur = cur.next
                    if cur == None:
                        curp.next = nnew
                    else:
                        curp.next = nnew
                        nnew.next = cur
                compare = compare.next
                curp = new
                cur = new.next
            return new
