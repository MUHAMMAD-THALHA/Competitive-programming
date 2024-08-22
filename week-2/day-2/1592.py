# Re-arrange space between words.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        
        total_spaces = text.count(' ')
    
        num_words = len(words)
        
        if num_words == 1:
       
            return words[0] + ' ' * total_spaces
        
       
        spaces_between_words = total_spaces // (num_words - 1)
        extra_spaces = total_spaces % (num_words - 1)
        
        
        result = (' ' * spaces_between_words).join(words)
        
       
        result += ' ' * extra_spaces
        
        return result


solution = Solution()
text = "  this   is  a sentence "
print(solution.reorderSpaces(text)) 
