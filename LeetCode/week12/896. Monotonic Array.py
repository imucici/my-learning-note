class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        s = sorted(A)
        d = sorted(A,reverse = True)
        if s == A or d == A:
            return True
        else:
            return False
