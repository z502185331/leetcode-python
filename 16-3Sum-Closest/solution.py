class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        nums.sort()
        m = len(nums)
        closest_num = sys.maxint
        
        # three pointer
        for i in xrange(m - 2):
            l, r = i + 1, m - 1;
            while l < r:
                
                # filter out same number
                # while l < r and l != i + 1 and nums[l] == nums[l - 1]:
                #     l += 1
                
                # while l < r and r != m - 1 and nums[r] == nums[r + 1]:
                #     r -= 1
                
                local = nums[i] + nums[l] + nums[r]
                if local == target:
                    print nums[i], nums[l], nums[r]
                    return local
                
                elif local < target:
                    l += 1
                
                else:
                    r -= 1
                
                # check the defference
                if abs(local - target) < abs(closest_num - target):
                    closest_num = local
        
        return closest_num
                    
                
        