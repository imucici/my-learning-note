# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lst: List[ListNode]) -> ListNode:
        if lst == []:
            return None
        else:
            a = []
            for i in range(len(lst)):
                head = lst[i]
                cur = head
                while cur != None:
                    a.append(cur.val)
                    cur = cur.next
            a = sorted(a)
            
            if len(a) == 0:
                return None
            else:
                head = ListNode(a[0])
                temp = head
                for i in range(1,len(a)):
                    temp.next = ListNode(a[i])
                    temp = temp.next
                return head
