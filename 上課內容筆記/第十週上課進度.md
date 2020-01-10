BST
=====

目錄:
---
* [程式碼](#程式碼)
* [leetcode](#leetcode)

程式碼:
-----

繼上次430行程式碼後，決定把邏輯重新想過，再次重寫一次作業

```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def insert(self,root,val):
        if val == root.val:
            new = TreeNode(val)
            new.left = root.left
            root.left = new
            #print("下面有節點的情況下，將相同的節點加到左邊")
            return root.left
        elif val < root.val: #跑到左邊
            if root.left == None:
                root.left = TreeNode(val)
                #print("新節點加到左邊")
                return root.left
            else:
                return Solution().insert(root.left,val)  
        elif val > root.val: #跑到右邊
            if root.right == None:
                root.right = TreeNode(val)
                #print("新節點加到右邊")
                return root.right
            else:
                return Solution().insert(root.right,val)    
   
    def pre(self,root,arr): # root-->left-->right
        
        if root == None:
            return arr
        arr.append(root.val)
        if root.left != None:
            Solution().pre(root.left,arr)
        if root.right != None:
            Solution().pre(root.right,arr)
        return arr
            
    def delete(self,root,target):
        
        #刪除的位於頭節點
        if root.val == target:
            end = root.left
            while end != None and end.val == target: 
                end = end.left
            root.left = end
            
            if root.left != None and root.right == None: #只有左小孩
                root = root.left
                return root
            elif root.left == None and root.right != None: #只有右小孩
                root = root.right
                return root
            elif root.right == None and root.left == None: #沒有小孩
                root = None
                return None
            else: #左右都有小孩
                if root.left.right == None and root.right.left != None: #左小孩沒有右小孩;右小孩有左小孩
                    curp = root.right
                    cur = root.right.left
                    while cur.left != None:
                        curp = cur
                        cur = cur.left
                    curp.left = cur.right
                    cur.right = root.right
                    cur.left = root.left
                    root = None
                    return cur
                elif root.left.right != None: #只要左小孩有右小孩
                    curp = root.left
                    cur = root.left.right
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    curp.right = cur.left
                    cur.right = root.right
                    cur.left = root.left
                    root = None
                    return cur
                else: #左小孩沒有右小孩;右小孩沒有左小孩
                    root = root.left
                    return root
                
        #刪除的不位於頭節點
        else:
            #先找到要刪除的節點
            p = None
            d = root 
            while target != d.val:
                if target <= d.val:
                    if d.left == None:
                        return root
                    else:
                        p = d
                        d = d.left
                elif target > d.val:
                    if d.right == None:
                        return root
                    else:
                        p = d
                        d = d.right      

            end = d.left
            while end != None and end.val == target:
                end = end.left
            d.left = end
            if d.left != None and d.right == None: #只有左小孩
                if p.left != None and p.left == d:
                    p.left = d.left # pd斜率為正
                else:
                    p.right = d.left # pd斜率為負
                return root
            elif d.right != None and d.left == None: #只有右小孩
                if p.left != None and p.left == d:
                    p.left = d.right
                else:
                    p.right = d.right
                return root
            elif d.left == None and d.right == None: #沒有小孩
                d = None
                return root           
            else: #左右都有小孩
                if d.left.right == None and d.right.left != None:
                    curp = d.right
                    cur = d.right.left
                    while cur != None:
                        cur = cur.left
                    curp.left = cur.right
                    cur.left = d.left
                    cur.right = d.right
                    if p.left != None and p.left == d:
                        p.left = cur
                    else:
                        p.right = cur
                    return root
                elif d.left.right != None:
                    curp = d.left
                    cur = d.left.right
                    while cur != None:
                        cur = cur.right
                    curp.right = cur.left
                    cur.left = d.left
                    cur.right = d.right
                    if p.left != None and p.left == d:
                        p.left = cur
                    else:
                        p.right = cur
                    return root
                else:
                    d.left.right = d.right
                    p.left = d.left
                    return root
  
    def search(self,root,target): #因為助教要的是離root最近的target，因此只要找到第一個target就可以return 
        if target  == root.val:
            return root
        elif target < root.val :
            if root.left == None:
                return False
            else:
                return Solution().search(root.left,target)
        elif target > root.val:
            if root.right == None:
                return False
            else:
                return Solution().search(root.right,target)
            
    def modify(self,root,target,new_val):
        if target != new_val: 
            
            #修改的位於頭節點
            if target == root.val:
                Solution().insert(root,new_val)
                end = root.left
                while end != None and end.val == target:
                    end = end.left    
                    Solution().insert(root,new_val)
                return Solution().delete(root,target)               
            else: 
                p = None
                d = root 

                #先找到要刪除的那個node
                while target != d.val:
                    if target <= d.val:
                        if d.left == None:
                            return root
                        else:
                            p = d
                            d = d.left
                    elif target > d.val:
                        if d.right == None:
                            return root
                        else:
                            p = d
                            d = d.right
                            
                Solution().insert(root,new_val)
                curp = d.left
                while curp != None and curp.val == target:
                    curp = curp.left
                    Solution().insert(root,new_val)
                return Solution().delete(root,target)
        else:
            return root
 ```
 
 leetcode:
 ------
 
 為了對BST更熟悉，用課餘的時間將leetcode所有的BST題目抓出來寫一遍!!!
 
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/108.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/109.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/173.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/230.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/449.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/501.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/530.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/538.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/653.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/700.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/701.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/783.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/938.jpg)
 ![圖](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/98.jpg)
 
