# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root ==  None:
            return []
        else:
            return self.pre(root,[])
    def pre(self,root,arr):
        arr.append(root.val)
        if root.left:
            self.pre(root.left,arr)
        if root.right:
            self.pre(root.right,arr)
        return arr
