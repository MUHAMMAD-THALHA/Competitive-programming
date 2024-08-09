<<<<<<< HEAD
# Count pairs that form a complete day 1.

from collections import Counter

class Solution:
    def countCompleteDayPairs(self, hours):
       
        remainders = [hour % 24 for hour in hours]
        
        freq = Counter(remainders)

        count = 0
    
        for r in freq:
           
            complement = (24 - r) % 24
            
            if complement in freq:
                if r == complement:
                 
                    count += freq[r] * (freq[r] - 1) // 2
                elif r < complement:
                  
                    count += freq[r] * freq[complement]
        
        return count

hours = [12, 12, 30, 24, 24]
solution = Solution()
print(solution.countCompleteDayPairs(hours)) 
=======
# Count pairs that forms a complete Day 1.
 
from collections import Counter

class Solution:
    def countCompleteDayPairs(self, hours):
       
        remainders = [hour % 24 for hour in hours]
        
        freq = Counter(remainders)

        count = 0
    
        for r in freq:
           
            complement = (24 - r) % 24
            
            if complement in freq:
                if r == complement:
                 
                    count += freq[r] * (freq[r] - 1) // 2
                elif r < complement:
                  
                    count += freq[r] * freq[complement]
        
        return count

hours = [12, 12, 30, 24, 24]
solution = Solution()
print(solution.countCompleteDayPairs(hours)) 
>>>>>>> 7b7328341ea8bd86372e5cf8b7dd65a33e5eb4cb
