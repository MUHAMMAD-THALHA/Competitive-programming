# MINIMUM NUMBER OF INCREMENTS ON SUBARRAYS TO FORM A TARGET ARRAY.

class Solution:
    def minNumberOperations(self, target):
        operations = target[0]  
        
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        
        return operations
target = [1, 2, 3, 2, 1]
solution = Solution()
print(solution.minNumberOperations(target))  
