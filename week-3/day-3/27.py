# Remove Element.

class Solution:
    def removeElement(self, nums, val):
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

# OUTPUT:
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(f'k = {k}, nums = {nums[:k]}')  
