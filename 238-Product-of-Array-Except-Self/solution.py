class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        m = len(nums)
        left_product = [1]
        right_product = [1]
        
        for i in xrange(1, m):
            left_product.append(left_product[-1] * nums[i - 1])
            
            j = m - i - 1
            right_product.insert(0, right_product[0] * nums[j + 1])
        
        res = []
        for i in xrange(m):
            res.append(left_product[i] * right_product[i])
        
        return res