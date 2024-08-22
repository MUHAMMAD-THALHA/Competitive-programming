# Find First and Last Position of Element in Sorted Araay.

class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first_occurrence = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    high = mid - 1  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first_occurrence
        
        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last_occurrence = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    low = mid + 1  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last_occurrence
        
        first_occurrence = findFirst(nums, target)
        last_occurrence = findLast(nums, target)
        
        return [first_occurrence, last_occurrence]

# OUTPUT.:
solution = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(solution.searchRange(nums, target))  
