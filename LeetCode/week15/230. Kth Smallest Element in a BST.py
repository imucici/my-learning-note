# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a = self.inorder(root,[])
        return a[k-1]
        
        
    def inorder(self,root,arr):
        if root.left != None:
            self.inorder(root.left,arr)
        arr.append(root.val)
        if root.right != None:
            self.inorder(root.right,arr)
        return arr
