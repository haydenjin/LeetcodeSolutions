# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def rangeSumBST(self, root, low, high):
        
        def bfs(node):

            if node:
                if low <= node.val <= high:
                    counter.append(node.val)

                if node.val > low:
                    bfs(node.left)

                if node.val < high:
                    bfs(node.right)


        counter = []

        bfs(root)

        return sum(counter)
