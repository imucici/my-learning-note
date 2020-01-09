# 題目:
# 費式數列

class Solution:
    def fib(self, N):
        a1 = 0
        a2 = 1
        for i in range(N):
            a3 = a1+a2
            a1 = a2
            a2 = a3
        return a1
