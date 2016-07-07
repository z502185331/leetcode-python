class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []
        
        groups = {}
        for word in strings:
            offsets = [0]   # based on first character
            for i in xrange(1, len(word)):
                prev = ord(word[i - 1])
                cur = ord(word[i])
                
                if cur < prev:
                    cur += 26
                
                offsets.append(cur - prev)
            pattern = tuple(offsets)
            
            groups[pattern] = groups.get(pattern, []) + [word]
        
        return [strings for strings in groups.values()]