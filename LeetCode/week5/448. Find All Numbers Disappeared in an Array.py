# 題目:
# 找出缺失值
# 例子:nums:[4,3,2,7,8,2,3,1]

class Solution:
    def findDisappearedNumbers(self, nums):
        sort = set(nums) #先刪除重複值
        a = [] #建一個正確的list
        for i in range(1,len(nums)+1):
            a.append(i)
        b = list(set(a)-sort) #找差集
        return b
