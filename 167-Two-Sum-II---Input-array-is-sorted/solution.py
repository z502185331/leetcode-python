class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not numbers:
            return [-1, -1]
        
        l, r = 0, len(numbers) - 1
        while l < r:
            num = numbers[l] + numbers[r]
            if num < target:
                l += 1
            elif num > target:
                r -= 1
            else:
                break
        
        return [l + 1, r + 1]
            