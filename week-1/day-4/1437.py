# CHECK IF ALL THE 1'S ARE AT LEAST ONES LENGTH K PASSES.

class Solution:
    def kLengthApart(self, nums, k):
        last_position = -1  

        for i, num in enumerate(nums):
            if num == 1:
                if last_position != -1 and i - last_position - 1 < k:
                    return False
                last_position = i
        
        return True


nums = [1,0,0,0,1,0,0,1]
k = 2
solution = Solution()
print(solution.kLengthApart(nums, k)) 
