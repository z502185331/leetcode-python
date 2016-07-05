class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return
        
        nums.sort()
        i, m = 1, len(nums)
        
        while i + 1 < m:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        