# Palindrome Partioning.

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        
        
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or palindrome[j + 1][i - 1]):
                    palindrome[j][i] = True
        
        
        dp = [float('inf')] * n
        
        for i in range(n):
            if palindrome[0][i]: 
                dp[i] = 0
            else:
                for j in range(i):
                    if palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]
