class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if nums is None or not nums:
            return []
        
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]
            
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    t = [nums[i], nums[l], nums[r]]
                    if t not in res:
                        res.append(t)
                    l += 1
                    r -= 1
        return res