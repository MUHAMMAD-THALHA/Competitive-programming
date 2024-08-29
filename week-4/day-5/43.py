# Multiply Strings.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit_multiplication = int(num1[i]) * int(num2[j])
                result[i + j] += digit_multiplication
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        

        result = result[::-1]
        return ''.join(map(str, result))

# OUTPUT
solution = Solution()
num1 = "2"
num2 = "3"
print(solution.multiply(num1, num2))  
