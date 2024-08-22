#ROTATE ARRAY.

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate the array to the right by k steps.
        This method modifies the array in place.
        """
        n = len(nums)
        k = k % n 
     
        if k == 0:
            return
        
      
        self.reverse(nums, 0, n - 1)
       
        self.reverse(nums, 0, k - 1)
       
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: list[int], start: int, end: int) -> None:
        """
        Reverse the elements in the list from start to end indices.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
print(nums) 
