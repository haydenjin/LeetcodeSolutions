# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDifference = 0

        self.dfs(root, root.val, root.val)

        return self.maxDifference

    def dfs(self, node, minVal, maxVal):
        if node != None:
            self.maxDifference = max(self.maxDifference, abs(minVal-node.val), abs(maxVal-node.val))
                
            # Update max and min
            maxVal = max(node.val, maxVal)
            minVal = min(node.val, minVal)

            self.dfs(node.left, minVal, maxVal)
            self.dfs(node.right, minVal, maxVal)
