# 題目:
#判斷是否為回文

# 觀念:
#[::-1] 適用於字串、[]
#----------------------------------------------------------------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = str(x) # 先將int轉成字串型態
        c = b[::-1] # [::-1]將字串順序反轉 
        if c == b :
            return True
        else:
            return False
