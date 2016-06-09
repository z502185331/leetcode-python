class SegmentNode(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.val = 0
        self.left = self.right = None
    
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        res = []
        root = self.build(min(nums), max(nums)) # build tree
        for num in reversed(nums):
            res.insert(0, self.query(root, num))
        return res
    
    '''
    A method to find the count of number smaller than it and change the val of node
    '''
    def query(self, node, num):
        if num == node.start and num == node.end:   # at leaf node
            node.val += 1
            return 0
        
        if num > node.end:
            return node.val
        
        if num < node.start:
            return 0
            
        mid = node.start + (node.end - node.start) / 2
        count = 0
        if num > mid:
            count = self.query(node.left, num) + self.query(node.right, num)
        else:
            count = self.query(node.left, num)
        node.val = node.left.val + node.right.val
        return count
        
    
    
    '''
    A method to build a segment tree
    @return the root of tree
    '''
    def build(self, start, end):
        node = SegmentNode(start, end)
        
        if start == end:
            return node
        
        mid = start + (end - start) / 2
        node.left = self.build(start, mid)
        node.right = self.build(mid + 1, end)
        return node