#Next Permutation.

class Solution:
    def nextPermutation(self, nums):
        """
        Rearranges numbers into the lexicographically next greater permutation.
        If such an arrangement is not possible, it rearranges it as the lowest possible order (i.e., sorted in ascending order).

        Args:
        nums (List[int]): A list of integers.

        Returns:
        None. The function modifies the list in place.
        """
        
        k = len(nums) - 2 
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        
        if k == -1:
     
            nums.reverse()
            return
        
        l = len(nums) - 1  
        while nums[l] <= nums[k]:
            l -= 1
        
        nums[k], nums[l] = nums[l], nums[k]
        
        nums[k + 1:] = reversed(nums[k + 1:])

# Output :
nums = [1, 2, 3]
solution = Solution()  
solution.nextPermutation(nums)
print(nums)  
