# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            a = self.inorder(root,[])

            if len(set(a)) == len(a):
                return a
            ans = [] 
            m = [] #紀錄當前最大的count
            count = 0
            for i in range(len(a)-1):
                if a[i] == a[i+1]:
                    count += 2
                    while i < len(a)-2 and a[i+1] == a[i+2]:
                        i += 1
                        count += 1
                    if len(ans) == 0:
                        ans.append(a[i])
                        m.append(count)
                    else:
                        if count > m[0]:
                            m[0] = count
                            ans = []
                            ans.append(a[i])
                        elif count == m[0]:
                            ans.append(a[i])
                    count = 0
            return ans
        
    def inorder(self,root,arr):
        if root.left != None:
            self.inorder(root.left,arr)
        arr.append(root.val)
        if root.right != None:
            self.inorder(root.right,arr)
        return arr
