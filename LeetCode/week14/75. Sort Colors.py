class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        while c < len(n)-1:
            for i in range(len(n)-1):
                if n[i]>n[i+1]:
                    n[i],n[i+1] = n[i+1],n[i]
            c+=1
