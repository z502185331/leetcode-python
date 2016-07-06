class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        self.pair = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        res = []
        self.dfs(digits, 0, res, [])
        return res
    
    def dfs(self, digits, index, res, path):
        if index == len(digits):
            res.append(''.join(path))
            return
        
        cur = self.pair[digits[index]]
        for c in cur:
            path.append(c)
            self.dfs(digits, index + 1, res, path)
            path.pop()
        