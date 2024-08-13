#Greatest COMMON DIVISOR.

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisible(s, t):
            if len(s) % len(t) != 0:
                return False
            return t * (len(s) // len(t)) == s

        gcd_length = self.gcd(len(str1), len(str2))
        candidate = str1[:gcd_length]

        if isDivisible(str1, candidate) and isDivisible(str2, candidate):
            return candidate
        else:
            return ""

str1 = "ABCABC"
str2 = "ABC"
solution = Solution()
print(solution.gcdOfStrings(str1, str2))  
