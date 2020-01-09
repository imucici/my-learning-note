class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = set()
        for i in range(len(nums)):
            if i > k:
                temp.remove(nums[i-k-1])
            if nums[i] in temp:
                return True
            temp.add(nums[i])
        return False
