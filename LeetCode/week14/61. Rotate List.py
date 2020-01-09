# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        else:
            
            arr = []
            size = 0
            cur = head
            while cur != None:
                arr.append(cur.val)
                cur = cur.next
                size+=1

            if size == k:
                a = arr
            elif size > k:
                a = arr[-k:]+arr[0:-k]
            else:
                p = k%size
                a = arr[-p:]+arr[0:-p]

            head = ListNode(a[0])
            temp = head
            for i in range(1,len(a)):
                temp.next = ListNode(a[i])
                temp = temp.next
            return head
