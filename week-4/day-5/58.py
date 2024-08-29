# Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')
        return len(words[-1])

# OUTPUT
solution = Solution()
s = "Hello World"
print(solution.lengthOfLastWord(s))
