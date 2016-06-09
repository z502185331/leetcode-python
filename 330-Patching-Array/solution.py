class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        
        i=0
        count=0
        s=1
        
        while s<=n:
            if i<len(nums) and s>=nums[i]:
                s+=nums[i]
                i+=1
            else:
                s<<=1
                count+=1
        return count
        