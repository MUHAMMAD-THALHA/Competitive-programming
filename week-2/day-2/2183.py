# Count Array Pairs Divisible by K.

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product % k == 0:
                    count += 1
        
        return count

solution = Solution()
nums = [1, 2, 3, 4, 5]
k = 2
print(solution.countPairs(nums, k))  


