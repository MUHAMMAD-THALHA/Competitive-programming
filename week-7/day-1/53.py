# Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize current_sum and max_sum with the first element
        current_sum = max_sum = nums[0]
        
        # Iterate over the array starting from the second element
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            # Update max_sum to track the largest sum found
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
result = solution.maxSubArray(nums)
print(result)  
