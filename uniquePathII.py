class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # dp[j] = ways to reach column j in the current row
        dp = [0] * n
        dp[0] = 1  # starting point
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # blocked cell → no ways
                elif j > 0:
                    dp[j] += dp[j-1]  # from left + from above
        
        return dp[-1]
