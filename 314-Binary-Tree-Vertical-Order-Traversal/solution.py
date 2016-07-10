# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        d = {}
        # self.traverse(root, 0, d)
        
        # BFS traverse tree layer by layer
        self.layerTraverse(root, d)
        
        # get the min and max idx of d
        res = []
        min_idx, max_idx = sys.maxint, -sys.maxint - 1
        for key in d:
            min_idx = min(min_idx, key)
            max_idx = max(max_idx, key)
            
        for i in xrange(min_idx, max_idx + 1):
            res.append(d[i])
        return res
    
    
    def layerTraverse(self, root, d):
        queue = [(root, 0)]
        while queue:
            size = len(queue)
            for _ in xrange(size):
                node, pos = queue.pop(0)
                d[pos] = d.get(pos, []) + [node.val]
                
                if node.left is not None:
                    queue.append((node.left, pos - 1))
                if node.right is not None:
                    queue.append((node.right, pos + 1))
                
        
    
    def traverse(self, node, pos, d):
        if node is None:
            return
        
        d[pos] = d.get(pos, []) + [node.val]
        self.traverse(node.left, pos - 1, d)
        self.traverse(node.right, pos + 1, d)