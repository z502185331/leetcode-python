from collections import defaultdict
class Solution(object):
    
    def groupAnagrams(self, strs):
    
        dic = defaultdict(list)
        for string in strs:
                dic[''.join(sorted(string))] += [string]
    
        return [value for key, value in dic.items()]
        