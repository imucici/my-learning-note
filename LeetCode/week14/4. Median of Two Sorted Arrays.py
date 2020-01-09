class Solution:
    def findMedianSortedArrays(self, n1, n2):
        m = sorted(n1+n2)
        if len(m)%2 != 0:
            return m[len(m)//2]
        else:
            return (m[len(m)//2]+m[len(m)//2-1])/2
