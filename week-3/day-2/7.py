# Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a signed 32-bit integer.
        
        Args:
        x (int): The input integer.
        
        Returns:
        int: The reversed integer, or 0 if the result overflows.
        """
        INT_MAX = 2**31 - 1  
        INT_MIN = -2**31    
        reversed_num = 0
        sign = 1
        
        if x < 0:
            sign = -1
            x = -x
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0
            
            reversed_num = reversed_num * 10 + digit
        return sign * reversed_num

# OUTPUT:
solution = Solution()
print(solution.reverse(123)) 
print(solution.reverse(-123))
print(solution.reverse(120)) 
print(solution.reverse(0))    
