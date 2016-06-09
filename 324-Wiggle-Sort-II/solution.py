class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        sorted_nums = sorted(nums)
        
        for i in range(1, m, 2) + range(0, m, 2):
            nums[i] = sorted_nums.pop()
        
        
        
        