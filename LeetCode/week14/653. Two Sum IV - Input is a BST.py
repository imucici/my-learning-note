# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root == None:
            return None
        else:
            arr = []
            a = Solution().pre(root,arr)
            
            for i in range(len(a)):
                for j in range(1,len(a)):
                    if i != j and a[i]+a[j]==k:
                        return True
            return False
    def pre(self,root,arr): 
        arr.append(root.val)
        if root.left != None:
            Solution().pre(root.left,arr)
        if root.right != None:
            Solution().pre(root.right,arr)
        return arr
            
