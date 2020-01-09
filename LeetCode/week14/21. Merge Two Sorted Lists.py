# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None and l2 == None:
            return None
        else:
            a1 = []
            cur1 = l1
            while cur1 !=None:
                a1.append(cur1.val)
                cur1 = cur1.next
            a2 = []
            cur2 = l2
            while cur2 !=None:
                a2.append(cur2.val)
                cur2 = cur2.next            

            s = sorted(a1+a2)

            head = ListNode(s[0])
            temp = head
            for i in range(1,len(s)):
                temp.next = ListNode(s[i])
                temp = temp.next
            return head
