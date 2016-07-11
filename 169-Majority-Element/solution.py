class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return None
        
        cur = None
        count = 0
        
        for num in nums:
            if cur == num:
                count += 1
            else:
                if count == 0:
                    cur = num
                else:
                    count -= 1
        
        return cur
                