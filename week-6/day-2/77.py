# COMBINATIONS

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination[:])
                return
            
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()
        
        backtrack(1, [])
        return result

# OUTPUT:
sol = Solution()
n = 4
k = 2
print(sol.combine(n, k))  
