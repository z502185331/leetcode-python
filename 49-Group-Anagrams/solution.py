class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        
        d = {}
        for str in strs:
            sort_str = ''.join(sorted(str))
            d[sort_str] = d.get(sort_str, []) + [str]
            
        return [value for value in d.values()]
        