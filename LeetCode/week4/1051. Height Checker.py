class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort= sorted(heights)
        nums = []
        for i in range(len(heights)):
            if heights[i] != sort[i]:
                nums.append(i)
                i+=1
        
        return len(nums)
