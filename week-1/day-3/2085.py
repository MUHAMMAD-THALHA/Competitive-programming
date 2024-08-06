#COUNT COMMON WORDS WITH ONE OCCURANCE

from collections import Counter

class Solution:
    def countWords(self, words1, words2):
        
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        result = 0
        
        for word in count1:
          
            if count1[word] == 1 and count2[word] == 1:
                result += 1
        
        return result

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
solution = Solution()
print(solution.countWords(words1, words2)) 
