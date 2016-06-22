class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return len(nums)
            
        
        m = len(nums)
        count = 1
        l = 1
        i = 1
        
        while i < m:
            if nums[i] != nums[i - 1]:
                nums[l] = nums[i]
                l += 1
                count = 1
            
            else:
                if count == 1:
                    nums[l] = nums[i]
                    l += 1
                    count = 2
            i += 1
        
        return l
        