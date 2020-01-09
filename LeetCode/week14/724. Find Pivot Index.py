class Solution(object):
	def pivotIndex(self, nums):
		if not nums or len(nums)==1:
			return -1
		t = sum(nums)
		sumtillnow = 0
		for i in range(0, len(nums)):
			if (t-nums[i])*0.5==sumtillnow:
				return i
			sumtillnow += nums[i]
		return -1
