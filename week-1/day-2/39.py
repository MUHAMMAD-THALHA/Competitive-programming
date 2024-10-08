# COMBINATION SUM

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result = []
        backtrack(0, target, [])
        return result


candidates = [2, 3, 6, 7]
target = 7
solution = Solution()
print(solution.combinationSum(candidates, target)) 
