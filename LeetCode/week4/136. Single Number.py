class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list1 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
            else :
                list1.remove(i)
        for k in list1:
            return k
