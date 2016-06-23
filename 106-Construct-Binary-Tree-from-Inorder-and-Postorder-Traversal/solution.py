# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or postorder is None or not inorder or not postorder:
            return None
        
        return self.build(inorder, 0, len(inorder) - 1, \
                            postorder, 0, len(postorder) - 1)
        
    '''
    A method to build the node by giving the range of in and post order
    @return : a treenode
    '''
    def build(self, inorder, in_start, in_end, postorder, post_start, post_end) :
        if in_start > in_end or post_start > post_end:
            return None
            
        if in_start == in_end or post_start == post_end:
            return TreeNode(inorder[in_start])
        
        # root node is at the end of postorder
        val = postorder[post_end]
        root = TreeNode(val)
        
        # find the position of root's val in inorder
        pos = inorder.index(val)
        root.left = self.build(inorder, in_start, pos - 1, \
                                    postorder, post_start, post_start + pos - in_start - 1)
        root.right = self.build(inorder, pos + 1, in_end, \
                                    postorder, post_start + pos - in_start, post_end - 1)
        return root