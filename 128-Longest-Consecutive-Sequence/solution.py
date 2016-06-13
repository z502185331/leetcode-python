class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        max_len = 0
        s1 = set()  # a set store all the nums
        s2 = set()  # a set store all the nums being processed
        
        # add all num to the set
        for num in nums:
            s1.add(num)
        
        for num in s1:
            # avoid repeated work
            if num in s2:
                continue
            s2.add(num)
            
            l = r = num
            while l - 1 in s1:
                l -= 1
                s2.add(l)
            
            while r + 1 in s1:
                r += 1
                s2.add(r)
            
            max_len = max(r - l + 1, max_len)
        return max_len
            
        