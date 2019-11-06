class Solution(object):
    def merge_sort(self,nums):
        self.nums = nums
        if len(nums) <= 1: #array為空或只有一個元素，默認已排序
            return nums
        else:
            half = len(nums)//2 #將array對半拆分成左右兩區塊
            left = nums[:half]
            right = nums[half:]
        
            print("left: ",left,",right:",right) #檢查拆分結果對不對
        
            while len(left) !=1: #拆分到每組array都剩一個元素就停止
                Solution().merge_sort(left)
                break
            while len(right) !=1: #拆分到每組array都剩一個元素就停止
                Solution().merge_sort(right)
                break
            
            n = 0
        
            while len(left) != 0 and len(right) != 0:
                if left[0] >= right[0]: #各拿左右兩邊array的第一個元素做比較
                    nums[n] = right[0] 
                    right.pop(0)#將比較完的數字從所屬array刪除，如此一來就可以永遠都用數組的第一個數做比較，可免去對left、right的index計數
                    n+=1
                else: #各拿左右兩邊array的第一個元素做比較
                    nums[n] = left[0]
                    left.pop(0)#將比較完的數字從所屬array刪除，如此一來就可以永遠都用數組的第一個數做比較，可免去對left、right的index計數
                    n+=1
            
            if len(left) == 0 and len(right) !=0:
                for i in range(len(right)): #看仍有元素的那個array長度多少，
                    nums.pop() #之後再依序將原始nums數組的元素，由後往前刪除
                nums.extend(right) #最後再將剩下的數組一併塞入nums，這樣才不會增加到原本的nums長度
            
            if len(right) == 0 and len(left) !=0:
                for i in range(len(left)):#看仍有元素的那個array長度多少，
                    nums.pop()#之後再依序將原始nums數組的元素，由後往前刪除
                nums.extend(left) #最後再將剩下的數組一併塞入nums，這樣才不會增加到原本的nums長度
            
        return nums
