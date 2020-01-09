# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        a = []
        cur = head
        while cur != None:
            a.append(cur.val)
            cur = cur.next
        m-=1
        n-=1
        
        h = a[:m]
        m = a[m:n+1]
        r = m[::-1]
        t = a[n+1:]
        final = h+r+t
        
        head = ListNode(final[0])
        temp = head
        for i in range(1,len(final)):
            temp.next = ListNode(final[i])
            temp = temp.next
        return head
