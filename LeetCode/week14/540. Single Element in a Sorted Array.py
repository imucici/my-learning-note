class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b = set(nums)
        return 2*sum(b)-sum(nums)
