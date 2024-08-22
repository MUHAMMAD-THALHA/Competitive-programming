# Move Zeroes..

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Moves all zeroes in nums to the end while maintaining the relative order of non-zero elements.
        This method modifies the list in place.
        """

        last_non_zero_index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index]
                last_non_zero_index += 1

# Output:
solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  
