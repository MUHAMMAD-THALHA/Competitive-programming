# Largest Odd Number In String..

class Solution:
    def largestOddNumber(self, num: str) -> str:
       
        for i in range(len(num) - 1, -1, -1):
            
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        
        return ""

# Output
sol = Solution()
print(sol.largestOddNumber("52"))  
