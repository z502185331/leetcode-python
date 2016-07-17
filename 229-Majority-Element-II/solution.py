class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        
        num1, num2 = 0, -1
        count1, count2 = 0, 0
        
        for num in nums:
            
            if num == num1:
                count1 += 1
            
            elif num == num2:
                count2 += 1
            
            elif count1 == 0:
                num1 = num
                count1 = 1
            
            elif count2 == 0:
                num2 = num
                count2 = 1
            
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            
            if num == num2:
                count2 += 1
        
        res = []
        if count1 > len(nums) / 3:
            res.append(num1)
        
        if count2 > len(nums) / 3:
            res.append(num2)
        
        return res
             