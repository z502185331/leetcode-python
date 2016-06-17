class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return None
        
        # [low, mid) [mid, mid], (mid, high)
        l, r = 1, len(nums) - 1
        while l < r:
            left_count = mid_count = right_count = 0
            mid = l + (r - l) / 2
            
            for num in nums:
                if num == mid:
                    mid_count += 1
                elif num < mid and num >= l:
                    left_count += 1
                elif num > mid and num <= r:
                    right_count += 1
            
            # print l, mid, r, left_count, mid_count, right_count
            if mid_count > 1:
                return mid
            elif left_count >= mid - l + 1:
                r = mid
            else:
                l = mid + 1
        
        return l