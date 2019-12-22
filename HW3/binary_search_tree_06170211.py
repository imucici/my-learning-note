class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    
    def pre(self,root,arr):
        if root:
            if root.left:
                self.pre(root.left,arr)
            arr.append(root.val)
            if root.right:
                self.pre(root.right,arr)
        return arr
    
    def insert(self,root,val):
        if root == None:
            new = TreeNode(val)
            root = new
            return root
        else:
            if root.val == val:
                new = TreeNode(val)
                new.left = root.left
                root.left = new
                return root
            elif root.val > val:
                if root.left == None:
                    new = TreeNode(val)
                    root.left = new
                    return root
                else:
                    return self.insert(root.left,val)
            else:
                if root.right == None:
                    new = TreeNode(val)
                    root.right = new
                    return root
                else:
                    return self.insert(root.right,val)
        
    def search(self,root,target):
        if root == None:
            return False
        else:
            if root.val == target:
                return True
            else:
                if root.val > val:
                    if root.left == None:
                        return False
                    else: self.search(root.left,target)
                else:
                    if root.right == None:
                        return False
                    else: self.search(root.right,target)
        
    def delete(self,root,target):
        if root:
            if root.val == target:
                end = root.left
                while end and end.val == target: 
                    end = end.left #調整成只有一個重複值
                root.left = end
                if root.left == None and root.right == None:
                    root = None
                    return root
                if root.left and root.right == None:
                    root = root.left
                    return root
                if root.right and root.left == None:
                    root = root.right
                    return root
                if root.left.right == None and root.right.left == None:
                    root.left.right = root.right
                    root = root.left
                    return root
                if root.left.right and root.right.left == None:
                    curp , cur = root.left , root.left.right
                    while cur.right:
                        curp = cur
                        cur = cur.right
                    curp.right = cur.left
                    cur.right = root.right
                    cur.left = root.left
                    root = None
                    return cur
                if root.right.left:
                    curp , cur = root.right , root.right.left
                    while cur.left:
                        curp = cur
                        cur = cur.left
                    curp.left = cur.right
                    cur.right = root.right
                    cur.left = root.left
                    root = None
                    return cur
            
            p , d = None , root
            while d and d.val != target:
                if d.val < target:
                    if d.right == None:
                        return root
                    else: 
                        p = d
                        d = d.right
                else:
                    if d.left == None:
                        return root
                    else:
                        p = d
                        d = d.left
            
            end = d.left
            while end and end.val == target: 
                end = end.left
                d.left = end
            if d.left == None and d.right == None:
                if p.left == d:
                    p.left = None
                    return root
                if p.right == d:
                    p.right = None
                    return root
            if d.left and d.right == None:
                if p.left == d:
                    p.left = d.left
                    return root
                if p.right == d:
                    p.right = d.left
                    return root
            if d.right and d.left == None:
                if p.left == d:
                    p.left = d.right
                    return root
                if p.right == d:
                    p.right = d.right
                    return root
            if d.left.right == None and d.right.left == None:
                if p.left == d:
                    d.left.right = d.right
                    p.left = d.left
                    return root
                if p.right == d:
                    d.left.right = d.right
                    p.right = d.left
                    return root
            if d.left.right and d.right.left == None:
                curp , cur = d.left , d.left.right
                while cur.right:
                    curp = cur
                    cur = cur.right
                curp.right = cur.left
                cur.right = d.right
                cur.left = d.left
                if p.right == d:
                    p.right = cur
                    return root
                if p.left == d:
                    p.left = cur
                    return root
            if d.right.left:
                curp , cur = d.right , d.right.left
                while cur.left:
                    curp = cur
                    cur = cur.left
                curp.left = cur.right
                cur.right = d.right
                cur.left = d.left
                if p.right == d:
                    p.right = cur
                    return root
                if p.left == d:
                    p.left = cur
                    return root

    def modify(self,root,target,new_val):
        if target != new_val:
            if root.val == target:
                end = root.left
                count = 1
                while end and end.val == target:
                    count += 1
                for i in range(count):
                    self.insert(root,new_val)
                return self.delete(root,target)
            
            p , d = None , root
            while d and d.val != target:
                if d.val < target:
                    if d.right == None:
                        return root
                    else: 
                        p = d
                        d = d.right
                else:
                    if d.left == None:
                        return root
                    else:
                        p = d
                        d = d.left
            count = 1
            end = d.left
            while end and end.val == target:
                end = end.left 
                count += 1
            for i in range(count):
                self.insert(root,new_val)
            return self.delete(root,target)
