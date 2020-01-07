class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = []
        b = []
        if k > len(nums):
            k = k % len(nums)
            b.extend(nums[-k:])
            a.extend(nums[:-k])
            b.extend(a)
            for i in range(len(nums)):
                if b[i] != nums[i]:
                    nums[i] = b[i]
            
        elif k <= len(nums):
            b.extend(nums[-k:])
            a.extend(nums[:-k])
            b.extend(a)

            for i in range(len(nums)):
                if b[i] != nums[i]:
                    nums[i] = b[i]
