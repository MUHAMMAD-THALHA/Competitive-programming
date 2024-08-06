# MINIMUM HOURS OF TRAINING TO WIN A COMPETITION.

from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        total_training_hours = 0
        
        for e, exp in zip(energy, experience):
            if initialEnergy <= e:
                total_training_hours += e - initialEnergy + 1
                initialEnergy = e + 1
            if initialExperience <= exp:
                total_training_hours += exp - initialExperience + 1
                initialExperience = exp + 1
            
            initialEnergy -= e
            initialExperience += exp
        
        return total_training_hours

initialEnergy = 5
initialExperience = 3
energy = [1, 4, 3, 2]
experience = [2, 6, 3, 1]
solution = Solution()
print(solution.minNumberOfHours(initialEnergy, initialExperience, energy, experience)) 
