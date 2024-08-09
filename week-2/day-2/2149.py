#RE-ARRANGE ARRAY ELEMENTS BY SIGN

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
      
        positives = []
        negatives = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        
        pos_index = 0
        neg_index = 0
        result = []
        
        while pos_index < len(positives) and neg_index < len(negatives):
            result.append(positives[pos_index])
            result.append(negatives[neg_index])
            pos_index += 1
            neg_index += 1
        
        return result

solution = Solution()
nums = [3, 1, -2, -5, 2, -4]
print(solution.rearrangeArray(nums))  

