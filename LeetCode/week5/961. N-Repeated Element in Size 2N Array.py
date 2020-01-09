# 題目:
# 找出重複的那個元素(int)
# A: List[int]

class Solution:
    def repeatedNTimes(self, A): 
        sort = list(set(A)) #先刪除重複元素
        return int((sum(A)-sum(sort))/(len(A)/2 -1 )) #透過元素總和算出所有重複值的和，再求單一一個元素為何
