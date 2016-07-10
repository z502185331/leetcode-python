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
            nums = [0] * k
            pos1, pos2, pos = 0, 0, 0
            while pos < k:
                if self.is_greater(subarray1, pos1, subarray2, pos2):
                    nums[pos] = subarray1[pos1]
                    pos1 += 1
                else:
                    nums[pos] = subarray2[pos2]
                    pos2 += 1
                
                pos += 1
            
            # compare the current nums with global result
            if self.is_greater(nums, 0, res, 0):
                res = nums
        
        return res
            
        
    
    def is_greater(self, nums1, idx1, nums2, idx2):
        """
        A method to check whether the nums1 from idx1 are greater than nums2 from idx2
        """
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] > nums2[idx2]:
                return True
            elif nums1[idx1] < nums2[idx2]:
                return False
            
            idx1 += 1
            idx2 += 1
            
        return idx1 != len(nums1)
    
    
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