class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        
        if not s:
            return
        
        self.reverse(s, 0, len(s) - 1)
        l = 0
        
        while l < len(s):
            if s[l] != ' ':
                r = l + 1
                while r < len(s) and s[r] != ' ':
                    r += 1
                
                self.reverse(s, l, r - 1)
                
                l = r
                
            l += 1

        
    def reverse(self, s, start, end):
        i, j = start, end
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1