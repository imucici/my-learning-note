# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:
        if a == None or b == None:
            return None
        else:
            
            len_a , temp_a = 0 , a
            while temp_a is not None:
                temp_a = temp_a.next
                len_a +=1
                
            len_b , temp_b = 0 , b
            while temp_b is not None:
                temp_b = temp_b.next
                len_b +=1
            
            while len_a > len_b :
                a = a.next
                len_a -=1
            
            while len_b > len_a :
                b = b.next
                len_b -=1
            
            if len_a == len_b:
                while a != b:
                    a = a.next
                    b = b.next
            return a
