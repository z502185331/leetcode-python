class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return None
        
        m = len(nums)
        nums = [-sys.maxint - 1] + nums + [-sys.maxint - 1] # add two number to prevent index out of bound
        l, r = 1, m
        
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            
            elif nums[mid] > nums[mid + 1]:
                r = mid - 1
        
        return l - 1
        
        
                
            