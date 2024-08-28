# Find the Index Of The First Occurence in a String.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# OUTPUT:
solution = Solution()
haystack = "sadbutsad"
needle = "sad"
print(solution.strStr(haystack, needle))
