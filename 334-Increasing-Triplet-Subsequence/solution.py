class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        m = len(nums)
        pair = [nums[0]]
        min_num = nums[0]
        for i in xrange(1, m):
            
            if len(pair) == 1:
                if nums[i] > pair[0]:
                    pair.append(nums[i])
                elif nums[i] < pair[0]:
                    pair[0] = nums[i]
            
            elif len(pair) == 2:
                if nums[i] > pair[1]:
                    return True
                
                if nums[i] < pair[0]:
                    if nums[i] > min_num:
                        pair[1], pair[0] = nums[i], min_num
                    
                    else:
                        min_num = nums[i]
                
                elif nums[i] > pair[0]:
                    pair[1] = nums[i]
        
        return False