# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        count = head
        size = 0
        while count != None:
            count = count.next
            size+=1

        recur = 0
        time = size-1
        coun = 0
        while recur < size-1:
            curp = head
            cur = head.next
            while cur!= None and coun < time:
                if curp.val > cur.val:
                    cur.val,curp.val = curp.val,cur.val
                curp = cur
                cur = cur.next
                coun += 1
            coun = 0
            time -= 1
            recur+=1
        return head
