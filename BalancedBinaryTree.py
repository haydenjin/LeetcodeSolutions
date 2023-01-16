# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return (self.tree(root) >= 0)


    
    def tree(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return 0

        leftHeight = self.tree(root.left)
        rightHeight = self.tree(root.right)

        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
            return -1

        # Get the largest side and add 1 
        largest = max(leftHeight, rightHeight) + 1

        return largest
