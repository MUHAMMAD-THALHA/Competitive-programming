# COMPLEMENT OF BASE 10 INTEGER.

class Solution:
    def bitwiseComplement(self, num: int) -> int:
        if num == 0:
            return 1
        
        bit_length = num.bit_length()
        bitmask = (1 << bit_length) - 1
        complement = num ^ bitmask
        return complement

num = 5
solution = Solution()
output = solution.bitwiseComplement(num)
print(f"The complement of {num} is {output}.")  

num = 0
output = solution.bitwiseComplement(num)
print(f"The complement of {num} is {output}.")  