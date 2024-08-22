# Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return         
        start, max_len = 0, 1
        def expandAroundCenter(left: int, right: int):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    start = left
                    max_len = current_len
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)
        return s[start:start + max_len]

# OUTPUT:
solution = Solution()
s = "babad"
print(solution.longestPalindrome(s))  
