# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return head
        else:  
            a = []
            while head != None:
                a.append(head.val)
                head = head.next
            return self.helper(a)
    
    def helper(self,a):
        if a:
            mid = len(a)//2
            root = TreeNode(a[mid])
            root.left = self.helper(a[:mid])
            root.right = self.helper(a[mid+1:])
            return root
