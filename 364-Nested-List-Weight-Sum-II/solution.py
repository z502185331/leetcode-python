# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        depth = self.getDepth(nestedList)
        return self.getSum(nestedList, depth)
        
    def getSum(self, nestedList, depth):
        """
        rtype: int
        """
        res = 0
        
        for item in nestedList:
            if item.isInteger():
                res += item.getInteger() * depth
            else:
                res += self.getSum(item.getList(), depth - 1)
        
        return res
    
    
    def getDepth(self, nestedList):
        depth = 1
        for item in nestedList:
            if not item.isInteger():
                depth = max(depth, self.getDepth(item.getList()) + 1)
        
        return depth
        