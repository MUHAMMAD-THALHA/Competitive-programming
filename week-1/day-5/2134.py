#Minimum Swaps To Group All 1's Together.

class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        total_ones = sum(nums)
        
        if total_ones == 0 or total_ones == n:
            return 0

        min_swaps = float('inf')
        current_zeros = sum(1 for i in range(total_ones) if nums[i] == 0)
        
        min_swaps = min(min_swaps, current_zeros)
        
        for i in range(1, n):
            if nums[i - 1] == 0:
                current_zeros -= 1
            if nums[(i + total_ones - 1) % n] == 0:
                current_zeros += 1
                
            min_swaps = min(min_swaps, current_zeros)
        
        return min_swaps


nums = [0,1,0,1,1,0,0]
solution = Solution()
print(solution.minSwaps(nums))  
