class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return None
        
        if nums[0] < nums[-1]:  # the list is sorted
            return nums[0]
        
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if nums[mid] >= nums[0]:
                l = mid
            
            elif nums[mid] < nums[0]:
                r = mid
        
        return nums[r]