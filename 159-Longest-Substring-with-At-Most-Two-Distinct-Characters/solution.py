class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        m = len(s)
        l, r = 0, 0
        max_len = 0
        count = {}
        
        while r < m:
            cur = s[r]
            count[cur] = count.get(cur, 0) + 1
            
            while len(count) > 2:
                cur = s[l]
                count[cur] -= 1
                
                if count[cur] == 0:
                    del count[cur]
                
                l += 1
                
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
        