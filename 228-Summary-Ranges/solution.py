class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        if not nums:
            return []
        
        ans = []
        m = len(nums)
        nums.append(sys.maxint) # add a elem to prevent index out of bound
        start, end = 0, 0
        for i in xrange(m):
            if nums[i + 1] == nums[i] + 1:
                end = i + 1
            else:
                if start == end:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + '->' + str(nums[end]))
                start = end = i + 1
        
        # deal with the situation when nums[-2] == sys.maxint - 1
        # if start != end:
        #     ans.append(str(nums[start]) + '->' + str(nums[end - 1]))
        
        return ans