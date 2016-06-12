class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        
        if not s or not wordDict:
            return []
        
        dict = {'' : ['']}
        m = len(s)
        
        def dfs(target):
            if target in dict:
                return dict[target]
            
            sol = []
            for word in wordDict:
                if word == target[: len(word)]:
                    for next_word in dfs(target[len(word) :]):
                            sol.append(word + ' ' + next_word if next_word else word)
            
            dict[target] = sol
            return sol
        
        dfs(s)
        return dict[s]
                
        
        
    
    def sol_2_dp(self, s, wordDict):
        m = len(s)
        dp = [[] for i in xrange(m + 1)]
        dp[0].append('')
        
        for i in xrange(m):
            for j in xrange(i + 1):
                cur = s[j : i + 1]
                if dp[j] and cur in wordDict:
                    if j == 0:
                        dp[i + 1].append(cur)
                    else:
                        for word in dp[j]:
                            dp[i + 1].append(word + ' ' + cur)
        return dp[-1]
    
    
    '''
    A method to recursively get the result, but LTE
    '''
    def sol_1_LTE(self, s, wordDict):
        res = []
        
        def dfs(index, path):
            if index == len(s):
                res.append(' '.join(path))
                return
            
            for i in xrange(index + 1, len(s) + 1):
                word = s[index : i]
                if word in wordDict:
                    path.append(word)
                    dfs(i, path)
                    path.pop()
        
        dfs(0, [])
        return res