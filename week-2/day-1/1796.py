# SECOND LARGEST DIGIT IN A STRING.

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for char in s:
            if char.isdigit():
                digits.add(int(char))
        
        sorted_digits = sorted(digits, reverse=True)
        
      
        if len(sorted_digits) >= 2:
            return sorted_digits[1]
        else:
            return -1

solution = Solution()
s = "dfa12321afd"
result = solution.secondHighest(s)
print(result)  
