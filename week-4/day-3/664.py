# Strange Printer.

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n + 1): 
            for i in range(n - length + 1):
                j = i + length - 1
                if i == j:
                    dp[i][j] = 1  
                else:
                    dp[i][j] = dp[i + 1][j] + 1
                
                    for k in range(i + 1, j + 1):
                        if s[i] == s[k]:
                            left = dp[i + 1][k - 1] if k - 1 >= i + 1 else 0
                            dp[i][j] = min(dp[i][j], left + dp[k][j])
        
        return dp[0][n - 1]

# OUTPUT:
solution = Solution()
s = "aaabbb"
print(solution.strangePrinter(s)) 
