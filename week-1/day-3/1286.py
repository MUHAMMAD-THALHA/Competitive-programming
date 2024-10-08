#ITERATOR FOR COMBINATION.

import itertools

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = list(itertools.combinations(characters, combinationLength))
        self.index = 0

    def next(self) -> str:
        combination = ''.join(self.combinations[self.index])
        self.index += 1
        return combination

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)


itr = CombinationIterator("abc", 2)
print(itr.next())    
print(itr.hasNext()) 
print(itr.next())    
print(itr.hasNext()) 
print(itr.next())    
print(itr.hasNext()) 
