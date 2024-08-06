#ADD TO ARRAY FORM OF INTEGER.

class Solution:
    def addToArrayForm(self, num, k):
        num_int = 0
        for digit in num:
            num_int = num_int * 10 + digit
        result_int = num_int + k
        result_array = [int(digit) for digit in str(result_int)]
        
        return result_array

num = [1,2,0,0]
k = 34
solution = Solution()
print(solution.addToArrayForm(num, k)) 
