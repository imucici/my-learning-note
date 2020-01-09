class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sum(nums) - sum(set(nums))
        l = len(nums)-len(set(nums))
        return s//l
