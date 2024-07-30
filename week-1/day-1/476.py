# NUMBER OF COMPLEMENT:

class Solution:
    def findComplement(self, num: int) -> int:
        binary_representation = bin(num)[2:]
        complement_representation = ''.join('1' if bit == '0' else '0' for bit in binary_representation)
        complement_num = int(complement_representation, 2)
        return complement_num
num = 5
solution = Solution()
output = solution.findComplement(num)
print(f"The complement of {num} is {output}.") 
