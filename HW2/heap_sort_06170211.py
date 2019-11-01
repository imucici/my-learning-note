#文字說明用上方的關係圖呈現
#("數字")代表關係圖上面的第幾個步驟

class Solution(object):
    
    #呼叫buildmaxheap，取得buildmaxheap回傳的值
    #再由buildmaxheap的值，經過呼叫siftdown來排序，最後取得排序完成的結果
    def heap_sort(self,nums):
        self.nums = nums
        maxheap = Solution().buildmaxheap(nums) #(1) / maxheap是第(4)步回傳回來的結果
        siftdown = Solution().siftdown(maxheap) #(5)
        return siftdown #(8)
    
    
    #呼叫maxheapify，取得maxheapify回傳的值
    def buildmaxheap(self,nums):
        n = len(nums)
        for i in reversed(range(0,n//2)):
            Solution().maxheapify(nums,n,i) #(2)
        return nums #(3)
    
    #呼叫maxheapify，取得maxheapify回傳的值
    def siftdown(self,nums):
        n = len(nums)
        for j in reversed(range(1,n)):
            nums[0],nums[j] = nums[j],nums[0]
            Solution().maxheapify(nums,j,0) #(6)
        return nums #(7)
    
    def maxheapify(self,nums,n,i):
        l = 2*i+1
        r = 2*i+2
        largest = i
        if l<n and nums[largest]<nums[l]:
            largest = l
        if r<n and nums[largest]<nums[r]:
            largest = r
        if largest != i:
            nums[largest],nums[i] = nums[i],nums[largest]
            Solution().maxheapify(nums,n,largest)
