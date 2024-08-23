# Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

# OUTPUT:
solution = Solution()
nums = [1, 1, 2]
k = solution.removeDuplicates(nums)
print(k)  
print(nums[:k])  
