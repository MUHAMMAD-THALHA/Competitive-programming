# Fraction Addition and Subtraction.

from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        fractions = expression.replace('-', '+-').split('+')
        result_num = 0
        result_den = 1
        
        for frac in fractions:
            if frac:
                num, den = map(int, frac.split('/'))
                result_num = result_num * den + num * result_den
                result_den *= den
                g = gcd(abs(result_num), result_den)
                result_num //= g
                result_den //= g
        
        return f"{result_num}/{result_den}"

# OUTPUT
solution = Solution()
expression = "-1/2+1/2"
print(solution.fractionAddition(expression))  
