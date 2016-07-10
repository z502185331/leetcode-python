class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ''
        
        stack = []
        m = len(s)
        counts = {}
        
        # count the characters in s
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        for c in s:
            if c in stack:
                counts[c] -= 1
                continue
                
            while stack and ord(c) < ord(stack[-1]) and counts[stack[-1]] > 0:
                stack.pop()
            
            stack.append(c)
            counts[c] -= 1
        
        return ''.join(stack)