class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        m = len(s)
        
        while i < m:
            length = 0
            while s[i] != '#':
                length = 10 * length + int(s[i])
                i += 1
            res.append(s[i + 1 : i + length + 1])
            
            i += length + 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))