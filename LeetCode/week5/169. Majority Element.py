# 題目:
# 找出出現最多次的數
# nums: List[int]

class Solution:
    def majorityElement(self, nums):
        from collections import Counter
        count = Counter(nums)
        a = dict(count.most_common())
        return max(a, key=a.get)
