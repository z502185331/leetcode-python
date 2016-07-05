class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return 0
        
        nums.sort()
        m = len(nums)
        count = 0
        for i in xrange(m - 2):
            l, r = i + 1, m - 1
            
            while l < r:
                sum_three = nums[i] + nums[l] + nums[r]
                if sum_three < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count
        