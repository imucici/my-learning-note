# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root == None or (root.left == None and root.right == None):
            return root
        else:
            self.sum = 0 
            return self.helper(root)
            
    def helper(self,root):
        if root.right != None:
            self.helper(root.right)
        self.sum+=root.val
        root.val = self.sum
            
        if root.left != None:
            self.helper(root.left)
        return root
