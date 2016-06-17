class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
            
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        
        return n * (n + 1) / 2 - sum
                    