# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root == None or (root.left == None and root.right == None):
            return root
        else:
            a = Solution().inorder(root,[])
            root = TreeNode(a[0])
            cur = root
            a.pop(0)
            
            while len(a) > 0:
                cur.right = TreeNode(a[0])
                a.pop(0)
                cur = cur.right
            return root
            
    def inorder(self,root,arr):
        if root.left != None:
            self.inorder(root.left,arr)
        arr.append(root.val)
        if root.right != None:
            self.inorder(root.right,arr)
        return arr
