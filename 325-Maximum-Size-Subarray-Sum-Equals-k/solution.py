class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
    
        if not nums:
            return 0
        
        m = len(nums)
        
        # create sumList, sumList[i] = nums[0] + ... + nums[i]
        sumList = []
        for num in nums:
            if not sumList:
                sumList.append(num)
            else:
                sumList.append(num + sumList[-1])
        
        # create dict for each sum, store the smallest index
        d = {0 : -1}
        for i, s in enumerate(sumList):
            if s not in d:
                d[s] = i
        
        # traverse the nums, find the result
        res = 0
        for i in xrange(m):
            if sumList[i] - k in d and d[sumList[i] - k] < i:   # find the target
                res = max(res, i - d[sumList[i] - k])
        
        return res
            