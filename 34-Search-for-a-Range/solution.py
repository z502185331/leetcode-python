class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not nums or target not in nums:
            return [-1, -1]
        
        m = len(nums)
        l, r = 0, m - 1
        start, end = -1, -1
        
        # find the left border of target
        while l + 1 < r:
            mid = l + (r - l) / 2
            if nums[mid] >= target:
                r = mid
            elif nums[mid] < target:
                l = mid
        
        start = l if nums[l] == target else r
        
        # find the right border of target
        l, r = 0, m - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        
        end = r if nums[r] == target else l
        
        return [start, end]