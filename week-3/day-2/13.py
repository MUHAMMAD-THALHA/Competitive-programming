# Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral to an integer.
        
        Args:
        s (str): The Roman numeral as a string.
        
        Returns:
        int: The integer representation of the Roman numeral.
        """
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):

            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        
        return total

# OUTPUT..:
solution = Solution()
print(solution.romanToInt("III"))    
print(solution.romanToInt("IV"))     
print(solution.romanToInt("IX"))     
print(solution.romanToInt("LVIII"))  
print(solution.romanToInt("MCMXCIV"))
