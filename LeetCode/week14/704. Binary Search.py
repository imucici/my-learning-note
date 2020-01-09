class Solution:
    def search(self, nums: List[int], t: int) -> int:
        for i in range(len(nums)):
            if nums[i] == t:
                return i
            
        return -1
