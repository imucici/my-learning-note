# 題目:
# 計算每個元素出現個數是否唯一

class Solution:
    def uniqueOccurrences(self, arr: List[int]):
        s = set(arr)
        list1 = []
        for i in s :
            list1.append(arr.count(i)) #藉由轉成set來得知arr有哪些元素，並透過s裡的元素計算arr裡各元素分別出現的次數
        new = set(list1)
        if len(new) == len(list1): #將計數後的list1轉成set，因為轉set後會刪除重複，若兩者長度不同就代表有刪除重複>>false
            return True
        else:
            return False
