class Solution:
    def thirdMax(self, n) -> int:
        if len(set(n)) < 3:
            return max(n)
        else:
            s = list(set(n))
            s = sorted(s,reverse = True)
            return s[2]
