# Number of Senior Citizens.

class Solution:
    def countSeniors(self, details):
        count = 0
        
        for detail in details:
            if len(detail) == 15:
                age_str = detail[11:13]
                try:
                    age = int(age_str)
                    if age > 60:
                        count += 1
                except ValueError:
                    continue  
        
        return count

# OUTPUT:
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
solution = Solution()
print(solution.countSeniors(details))

invalid_details = [" ", " ", " "]
print(solution.countSeniors(invalid_details))  
