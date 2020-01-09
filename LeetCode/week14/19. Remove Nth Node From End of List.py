# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next == None:
            return None
        else:
            
            a = []
            cur = head
            while cur != None:
                a.append(cur.val)
                cur = cur.next
            a.pop(-n)
            
            head = ListNode(a[0])
            temp = head
            for i in range(1,len(a)):
                temp.next = ListNode(a[i])
                temp = temp.next
            return head
