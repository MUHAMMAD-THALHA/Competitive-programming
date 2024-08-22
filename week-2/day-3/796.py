# Rotate String..

class Solution:
    @staticmethod
    def rotateString(s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        concatenated_s = s + s
        return goal in concatenated_s

# Output.
s = "abcde"
goal = "cdeab"
solution = Solution()
print(solution.rotateString(s, goal)) 
