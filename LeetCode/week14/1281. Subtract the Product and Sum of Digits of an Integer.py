class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = str(n)
        m = 1
        s = 0
        for i in a :
            m*=int(i)
            s+=int(i)
        final = m-s
        return final
