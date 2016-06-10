# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = [root]
        
        while queue:    # traverse all nodes level by level
            size = len(queue)
            for i in xrange(size):
                node = queue.pop(0)
                if node is not None:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                    
                else:   # '#' shows that the node is None
                    res.append('#')
        
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        queue = []
        
        root = None
        if l[0] == '#': # empty tree
            return None
        else:
            root = TreeNode(l.pop(0))
            queue.append(root)
            
        while l:
            left_node = right_node = None
            
            if l[0] != '#':
                left_node = TreeNode(l[0])
                queue.append(left_node)
            l.pop(0)
            
            if l[0] != '#':
                right_node = TreeNode(l[0])
                queue.append(right_node)
            l.pop(0)
            
            node = queue.pop(0)
            node.left = left_node
            node.right = right_node
        
        return root
            
            
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))