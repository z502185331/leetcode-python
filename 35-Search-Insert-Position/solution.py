class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return 0
        
        m = len(nums)
        l, r = 0, m - 1
        
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return l