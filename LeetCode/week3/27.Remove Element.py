# 題目:
#在list中刪除等於val的元素，並計算出新的list長度
# nums: List[int], val: int

# 例子:
#nums = [3,2,2,3], val = 3

# 觀念:
# a = [1,2,3,1,2,3]
# a.remove(2) #remove() 僅移除第一個出現的特定值
# 結果:[1, 3, 1, 2, 3]

# b = [1,2,3,1,2,3]
# print(b.pop(2)) #回傳位於第2個位置的值。結果:3
# print(b) #移除位於第2個位置的元素，並列出完整列表。結果:[1, 2, 1, 2, 3]
#------------------------------------------------------------------
#code:
#[解一]
class Solution:
    def removeElement(self, nums, val) -> int:
        for i in range(len(nums)-1,-1,-1): # 也就是 for i in [3,2,1,0] >>此為序號
            if nums[i] == val:             #跑出來的結果:nums[3],nums[2],nums[1],nums[0](=3,2,2,3)
                nums.remove(val)
        return(len(nums))
#[解二]
class Solution:
    def removeElement(self, nums, val) -> int:
        for i in nums:  # 也就是 for i in [3,2,2,3] >>此為原始list
            if i == val:             #跑出來的結果:3,2,2,3
                nums.remove(val)
        return(len(nums))
