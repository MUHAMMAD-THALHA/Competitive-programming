# BACKSPACE STRING COMPARE.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string: str) -> str:
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()  
                else:
                    stack.append(char) 
            return ''.join(stack)  

        return processString(s) == processString(t)  

s = "ab#c"
t = "ad#c"
solution = Solution()
print(solution.backspaceCompare(s, t))  
