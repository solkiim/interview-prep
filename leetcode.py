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
