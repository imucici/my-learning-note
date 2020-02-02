# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        temp = []
        cur = head
        while cur != None:
            temp.append(cur.val)
            cur = cur.next
        
        even = []
        odd = []
        for i in range(len(temp)):
            if i % 2 == 0:
                even.append(temp[i])
            else:
                odd.append(temp[i])
        
        count = 0
        head = ListNode(odd[0])
        odd.pop(0)
        current = head
        
        while len(even) != 0 and len(odd) != 0 :
            current.next = ListNode(even[0])
            even.pop(0)
            current = current.next
            current.next = ListNode(odd[0])
            odd.pop(0)
            current = current.next
            
        if len(even) != 0 and len(odd) == 0:
            if len(even) % 2 == 0 :
                current.next = ListNode(even[0])
                current = current.next
                current.next = ListNode(even[-1])
            else:
                current.next = ListNode(even[0])
                current = current.next
                
        if len(even) == 0 and len(odd) != 0:
            if len(odd) % 2 == 0 :
                current.next = ListNode(odd[0])
                current = current.next
                current.next = ListNode(odd[-1])
            else:
                current.next = ListNode(odd[0])
                current = current.next
        return head
