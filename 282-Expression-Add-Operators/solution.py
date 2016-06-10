class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        if not num:
            return []
        
        res = []
        self.dfs(num, target, 0, 0, 0, None, '', res)
        return res
        
    '''
    A method to find out all the answers by dfs
    @param last_res the result calculated by previous expression
    @param last_num the previous number to deal with *, it can be negative if the previous operator is '-'
    '''
    def dfs(self, num, target, index, last_res, last_num, last_oper, path, res):
        if index == len(num):
            if last_res == target:
                res.append(path)
            return
        
        for i in xrange(index, len(num)):
            if num[index] == '0' and i != index:    # any number except 0 will not start with 0
                break
            
            cur_num = int(num[index : i + 1])
            
            # check whether this is the first expression
            if not path:
                self.dfs(num, target, i + 1, cur_num, cur_num, None, str(cur_num), res)
                continue
            
            # multiply cur_num
            self.dfs(num, target, i + 1, last_res - last_num + last_num * cur_num, \
                                last_num * cur_num, '*', path + '*' + str(cur_num), res)
                
            # add cur_num
            self.dfs(num, target, i + 1, last_res + cur_num, cur_num, '+', path + '+' + str(cur_num), res)
            
            # minus cur_num
            self.dfs(num, target, i + 1, last_res - cur_num, -cur_num, '-', path + '-' + str(cur_num), res)
            
            