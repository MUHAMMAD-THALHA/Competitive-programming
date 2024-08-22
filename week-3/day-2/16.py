# 3 Sum Closest.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        Finds the sum of three integers in nums that is closest to the given target.
        
        Args:
        nums (List[int]): List of integers.
        target (int): The target sum.
        
        Returns:
        int: The sum of the three integers closest to the target.
        """
        
        nums.sort()  
        closest_sum = float('inf')  
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1  
                elif current_sum > target:
                    right -= 1  
                else:
                    return current_sum
        
        return closest_sum  

# OUTPUT:
solution = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(solution.threeSumClosest(nums, target))  
