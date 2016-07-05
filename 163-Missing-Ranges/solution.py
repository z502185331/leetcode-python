class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
    
        if nums is None or not nums:
            return [self.encode(lower, upper)]
        
        cur = lower
        res = []
        for num in nums:
            if num > upper:
                break
            
            if num < cur:   # num out of range
                continue
            
            elif num == cur:
                cur += 1
            
            else:
                res.append(self.encode(cur, num - 1))
                cur = num + 1
        
        if cur <= upper:
            res.append(self.encode(cur, upper))
        return res
    
    '''
    A method to encode the range
    '''
    def encode(self, start, end):
        if start > end:
            return ''
        
        if start == end:
            return str(start)
        
        else:
            return str(start) + '->' + str(end)