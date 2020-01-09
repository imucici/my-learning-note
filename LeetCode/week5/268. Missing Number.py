# 題目:
# 找缺失值(int)
# nums: List[int]

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return int((n+1)*n/2 - sum(nums)) #正確list值的總和 - nums總和 = 缺失值
