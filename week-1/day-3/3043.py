#FIND THE LENGTH OF THE LONGEST COMMON PREFIX

class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        def commonPrefixLength(a, b):
            a_str, b_str = str(a), str(b)
            i = 0
            while i < len(a_str) and i < len(b_str) and a_str[i] == b_str[i]:
                i += 1
            return i
        
        max_length = 0
        
        for x in arr1:
            for y in arr2:
                max_length = max(max_length, commonPrefixLength(x, y))
        
        return max_length


arr1 = [1, 10, 100]
arr2 = [1000]
solution = Solution()
print(solution.longestCommonPrefix(arr1, arr2))  
