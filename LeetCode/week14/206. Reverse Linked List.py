# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        else:
        
            a = []
            cur = head
            while cur != None:
                a.append(cur.val)
                cur = cur.next
            r = a[::-1]

            head = ListNode(r[0])
            temp = head
            for i in range(1,len(r)):
                temp.next = ListNode(r[i])
                temp = temp.next
            return head
