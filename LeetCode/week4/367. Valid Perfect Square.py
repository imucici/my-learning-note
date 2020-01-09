class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = num**(1/2)
        if (a).is_integer() :
            return True
        else:
            return False
            
