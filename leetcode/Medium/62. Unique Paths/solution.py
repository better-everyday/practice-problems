class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for x in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[m-1][n-1] = 1
                    continue

                try: bottom = dp[i+1][j]
                except: bottom = 0

                try: right = dp[i][j+1]
                except: right = 0

                dp[i][j] = bottom + right

        return dp[0][0]