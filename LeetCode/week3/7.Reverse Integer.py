# 題目:
#將整數反轉

#觀念:
#1.[::-1]不能用於int
#2.strip()函數可刪除特定值
#-------------------------------------------------------
class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)[::-1] ##反轉後
        if x <0:
            b = a.strip("-") #移除負號
            if int(b)>2**31-1:
                return 0
            else:
                return -int(b)
        
        else:
            if int(a) >2**31-1:
                return 0
            else:
                return int(a)
