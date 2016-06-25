class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
            
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, index, path, res):
        if len(path) == 4 or index == len(s):
            if len(path) == 4 and index == len(s):
                res.append('.'.join(path)) # join the path and put into res
            return
        
        for i in range(3):
            if index + i < len(s):
                num = s[index : index + i + 1]
                
                if int(num) <= 255:
                    path.append(num)
                    self.dfs(s, index + i + 1, path, res)
                    path.pop()
            
            # 010 001 is illegal, but 0 is legal
            if s[index] == '0':
                break