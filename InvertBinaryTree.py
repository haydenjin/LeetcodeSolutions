# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.tree(root)

    
    def tree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:

        if node != None:
            temp = node.left 
            node.left = node.right
            node.right = temp
            # Call on both side of tree recursively 
            self.tree(node.right)
            self.tree(node.left)

        return node
