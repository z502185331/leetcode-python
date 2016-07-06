class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        if not s:
            return 0
        
        # count the appearance of characters in k
        count = {}
        m = len(s)
        maxLen = 0
        
        l, r = 0, 0
        while r < m:
            cur = s[r]
            count[cur] = count.get(cur, 0) + 1
            
            while len(count) > k:
                cur = s[l]
                count[cur] -= 1
                if count[cur] == 0:
                    del count[cur]
                
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen