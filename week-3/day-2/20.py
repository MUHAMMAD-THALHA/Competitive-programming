#Valid Parenthesis..

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string of brackets is valid.
        
        Args:
        s (str): The input string containing brackets.
        
        Returns:
        bool: True if the string is valid, False otherwise.
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
            
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

# OUTPUT..
solution = Solution()
s = "()"
print(solution.isValid(s))  
