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
            
        res = []
        for l in d.values():
            res.append(l)
            
        return res
        