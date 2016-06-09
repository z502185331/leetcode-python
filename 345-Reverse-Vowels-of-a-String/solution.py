class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or not s:
            return s
        
        m = len(s)
        sl = list(s)
        l, r = 0, m - 1
        
        while l < r:
            while l < r and not self.isVowel(sl[l]):
                l += 1
            
            while r > l and not self.isVowel(sl[r]):
                r -= 1
                
            sl[l], sl[r] = sl[r], sl[l]
            l += 1
            r -= 1
        
        return ''.join(sl)
    
    '''
    A method to check whether a character is a vowel
    '''
    def isVowel(self, c):
        return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']