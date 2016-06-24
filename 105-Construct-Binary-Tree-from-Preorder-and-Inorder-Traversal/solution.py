# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if inorder is None or preorder is None or not inorder or not preorder:
            return None
        
        return self.build(inorder, 0, len(inorder) - 1, \
                            preorder, 0, len(preorder) - 1)
        
    
    '''
    A method to build the node by giving the range of in and pre order
    @return : a treenode
    '''
    def build(self, inorder, in_start, in_end, preorder, pre_start, pre_end) :
        
        if in_start > in_end or pre_start > pre_end:
            return None
            
        if in_start == in_end or pre_start == pre_end:
            return TreeNode(inorder[in_start])
        
        # root node is at the end of postorder
        val = preorder[pre_start]
        root = TreeNode(val)
        
        # find the position of root's val in inorder
        pos = inorder.index(val)
        root.left = self.build(inorder, in_start, pos - 1, \
                                preorder, pre_start + 1, pre_start + pos - in_start)
        root.right = self.build(inorder, pos + 1, in_end, \
                                    preorder, pre_start + pos - in_start + 1, pre_end)
        return root