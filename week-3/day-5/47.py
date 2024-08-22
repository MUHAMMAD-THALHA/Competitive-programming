#Permutations II

class Solution:
    def permuteUnique(self, nums):
        def backtrack(path, used):
            if len(path) == len(nums):
                results.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        
        results = []
        nums.sort()
        used = [False] * len(nums)
        backtrack([], used)
        return results

# OUTPUT:
solution = Solution()
nums = [1, 1, 2]
print(solution.permuteUnique(nums))
