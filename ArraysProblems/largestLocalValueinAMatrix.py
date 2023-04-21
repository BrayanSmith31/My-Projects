# You are given an n x n integer matrix grid.

# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

# Return the generated matrix.

# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]
# Explanation: The diagram above shows the original matrix and the generated matrix.
# Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid

class Solution:
    def largestLocal(self, grid):
        size = len(grid)-2
        ans = []
        for i in range(size):
            for j in range(size):
                max = grid[i][j]
                for ii in range(i,i+2):
                    for jj in range(j, j+2):
                        if grid[ii][jj]> max:
                            max = grid[ii][jj]
                ans[i][j] = max
        return ans

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
res = Solution()
res.largestLocal(grid)