class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sort = sorted(nums)
        list1 = []
        for i in range(0,len(sort),2):
            list1.append(sort[i])
        return sum(list1)
