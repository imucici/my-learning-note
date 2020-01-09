# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        if head == None:
            return None
        else:
            arr = []
            cur = head
            while cur != None:
                arr.append(cur.val)
                cur = cur.next

            arr = sorted(arr)

            head = ListNode(arr[0])
            temp = head
            for i in range(1,len(arr)):
                temp.next = ListNode(arr[i])
                temp = temp.next
            return head
