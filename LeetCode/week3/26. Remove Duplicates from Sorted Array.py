# 題目:
#刪除list中重複元素，並計算出新list長度
# nums: List[int]

#-------------------------------------------------------------
#[解一]
class Solution:
    def removeDuplicates(self, nums) -> int:
        newlist = []
        for i in nums:
            if i not in newlist:
                newlist.append(i)
        return len(newlist)         
#[解二]
class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] ==nums[i+1]:
                nums.remove(nums[i])
            else:
                i+=1
        return len(nums)
