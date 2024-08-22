# Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums, k):
        """
        Returns the total number of subarrays whose sum equals to k.
        
        Args:
        nums (List[int]): List of integers.
        k (int): The target sum.
        
        Returns:
        int: The number of subarrays that sum to k.
        """
        prefix_sum_count = {0: 1}  
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num

            if current_sum - k in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        
        return count

# OUTPUT:
nums = [1, 1, 1]
k = 2
output = Solution().subarraySum(nums, k)
print(output)  
