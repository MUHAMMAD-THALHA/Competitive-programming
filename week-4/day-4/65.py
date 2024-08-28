 # Valid Number.

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r"""
            ^[+-]?             
            (?:
                \d+\.\d* |       
                \.\d+  |         
                \d+              
            )
            (?:[eE][+-]?\d+)?$   
        """, re.VERBOSE)
        
        return bool(pattern.match(s))

# OUTPUT
solution = Solution()
s = "0"
print(solution.isNumber(s))
