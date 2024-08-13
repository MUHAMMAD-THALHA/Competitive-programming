#Number Of Ways To Stay in The Same Place After Some Steps.

class Solution:
    def numWays(self, steps, arrLen):
        MOD = 10**9 + 7
        max_col = min(arrLen, steps // 2 + 1)

        dp = [[0] * max_col for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(max_col):
                dp[i][j] = dp[i-1][j]  
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD  
                if j < max_col - 1:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD  

        return dp[steps][0]

steps = 3
arrLen = 2
solution = Solution()
print(solution.numWays(steps, arrLen)) 
