# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafs1 = []
        leafs2 = []

        self.dfs(root1, leafs1)
        self.dfs(root2, leafs2)

        if len(leafs1) != len(leafs2):
            return False
            
        for i in range(len(leafs1)):
            if leafs1[i] != leafs2[i]:
                return False

        return True

    def dfs(self, node, leafs):
        if node != None:
            if node.left == None and node.right == None:
                leafs.append(node.val)

            self.dfs( node.left, leafs)
            self.dfs( node.right, leafs)
