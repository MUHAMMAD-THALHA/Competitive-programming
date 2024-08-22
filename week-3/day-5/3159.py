# Find Occurence of an Element in an Array.

class Solution:
    def occurrencesOfElement(self, nums, queries, x): 
        occurrences = {}
        for i, num in enumerate(nums):
            if num == x:
                if x not in occurrences:
                    occurrences[x] = []
                occurrences[x].append(i)
        
        result = []
        
        for query in queries:
            if x in occurrences and query <= len(occurrences[x]):
                result.append(occurrences[x][query - 1])
            else:
                result.append(-1)
        
        return result

# OUTPUT:
solution = Solution()
nums = [1, 3, 1, 7]
queries = [1, 3, 2, 4]
x = 1
print(solution.occurrencesOfElement(nums, queries, x))
