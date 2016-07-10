class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        len1, len2 = len(nums1), len(nums2)
        res = [0] * k
        for i in xrange(max(0, k - len2), min(k, len1) + 1):
            subarray1 = self.get_max_subarray(nums1, i)
            subarray2 = self.get_max_subarray(nums2, k - i)
            
            # rearrnge two subarray to a nums with length k
            res = max(res, [max(subarray1, subarray2).pop(0) for _ in xrange(k)])
        
        return res
    
    
    def get_max_subarray(self, nums, k):
        """
        A method to get the max subarray while preserve the related position in nums
        """
        res = [0] * k
        cur = 0
        
        for i in xrange(len(nums)):
            while cur > 0 and cur + len(nums) - i > k and nums[i] > res[cur - 1]:
                cur -= 1
            
            if cur < k:
                res[cur] = nums[i]
                cur += 1
                
        return res