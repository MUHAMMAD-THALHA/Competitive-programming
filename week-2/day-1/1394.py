# Find Lucky Integer in an array.

class Solution:
    def findLucky(self, arr):
        freq_map = {}
        
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        largest_lucky = -1
        
        # Find the largest integer whose frequency matches its value
        for key, value in freq_map.items():
            if key == value:
                largest_lucky = max(largest_lucky, key)
        
        return largest_lucky

arr = [2, 2, 3, 4]  
solution = Solution()
result = solution.findLucky(arr)
print(f"The largest lucky integer in the array is: {result}")
