class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        a = []
        for i in range(len(nums)-1):
            if s[i] == s[i+1]:
                a.append(s[i])
        return a
