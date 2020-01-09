class Solution:
    def isPowerOfThree(self, n: int):
        if n == 1:
            return True
        elif n <= 0 or n%3 != 0:
            return False
        else:
            return self.isPowerOfThree(n/3)
