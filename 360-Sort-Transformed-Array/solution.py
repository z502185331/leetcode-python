class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        m = len(nums)
        res = [0] * m
        l, r = 0, m - 1
        index = 0 if a < 0 else m - 1
        
        while l <= r:
            num1 = self.eval(nums[l], a, b, c)
            num2 = self.eval(nums[r], a, b, c)
            
            if a < 0:
                if num1 < num2:
                    res[index] = num1
                    l += 1
                else:
                    res[index] = num2
                    r -= 1
                index += 1
            
            else:
                if num1 < num2:
                    res[index] = num2
                    r -= 1
                else:
                    res[index] = num1
                    l += 1
                
                index -= 1
        
        return res
        
        
        
    
    
    def eval(self, x, a, b, c):
        return a * x * x + b * x + c
        
    

            