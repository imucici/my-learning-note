# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root ==  None:
            return []
        else:
            return self.post(root,[])
    def post(self,root,arr):
        if root.left:
            self.post(root.left,arr)
        if root.right:
            self.post(root.right,arr)
        arr.append(root.val)
        return arr
