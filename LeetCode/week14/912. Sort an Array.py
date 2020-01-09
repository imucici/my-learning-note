class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
             return nums
        else:
            pivot = nums[0]
            smaller = []
            equal = []
            bigger = []
            for i in nums:
                if i < pivot:
                    smaller.append(i)
                elif i > pivot:
                    bigger.append(i)
                else:
                    equal.append(i)
        return Solution().sortArray(smaller)+equal+Solution().sortArray(bigger)
