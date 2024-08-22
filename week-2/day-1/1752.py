# CHECK IF ARRAY IS SORTED.

class Solution:
    def check(self, nums):
        n = len(nums)
        if n == 1:
            return True
        
        count_decrease = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                count_decrease += 1
                
        if count_decrease > 1:
            return False
        
        if count_decrease == 0:
            return True
        return nums[-1] <= nums[0]

solution = Solution()
nums = [3, 4, 5, 1, 2]
print(solution.check(nums))  
