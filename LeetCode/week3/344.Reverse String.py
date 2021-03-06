# 題目:
#將list內的元素反轉
#s: List[str]

# 觀念:
# list反轉後為原始list的副本;str反轉後會覆蓋掉原始的str
#-------------------------------------------------------------------------------------------------------------------------
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]  # [::-1]可用於字串、list。因為s為list，所以返回的為原始s的副本，因此要寫成s[:]。(若s為字串，則為同一對象)
