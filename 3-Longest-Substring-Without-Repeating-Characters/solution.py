class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        index_dict = {} # records the last index of the character
        max_len = 0
        cur_len = 0
        
        for i, c in enumerate(s):
            if c not in index_dict:
                cur_len += 1
            
            else:
                if index_dict[c] >= i - cur_len:
                    cur_len = i - index_dict[c]
                
                else:
                    cur_len += 1
            
            index_dict[c] = i
            max_len = max(max_len, cur_len)
        
        return max_len