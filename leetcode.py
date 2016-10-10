# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path
# from top left to bottom right which minimizes the sum of all numbers
# along its path.
# Note: You can only move either down or right at any point in time.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        dynArr = [[0] * len(grid[0]) for x in range(len(grid))]
        
        dynArr[0][0] = grid[0][0]
        
        for r in range(1, len(grid)):
            dynArr[r][0] = dynArr[r-1][0] + grid[r][0]

        for c in range(1, len(grid[0])):
            dynArr[0][c] = dynArr[0][c-1] + grid[0][c]
        
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                fromTop = dynArr[r-1][c]
                fromLeft = dynArr[r][c-1]
                dynArr[r][c] = min(fromTop, fromLeft) + grid[r][c]
                
        return dynArr[len(grid)-1][len(grid[0])-1]


# 104. Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the
# root node down to the farthest leaf node.
# -----
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if (root.left == None) and (root.right == None):
            return 1
        if (root.left == None):
            return self.maxDepth(root.right) + 1
        if (root.right == None):
            return self.maxDepth(root.left) + 1
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            return max(leftDepth, rightDepth) + 1
