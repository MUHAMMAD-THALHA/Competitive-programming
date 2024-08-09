<<<<<<< HEAD
from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def is_inside_circle(px, py, cx, cy, r):
            return (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2
        
        answer = []
        for cx, cy, r in queries:
            count = 0
            for px, py in points:
                if is_inside_circle(px, py, cx, cy, r):
                    count += 1
            answer.append(count)
        
        return answer

points = [[1, 3], [3, 3], [5, 3], [2, 2]]
queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
solution = Solution()
output = solution.countPoints(points, queries)
print(output)  
=======
#QUERIES ON NUMBER OF POINTS INSIDE A CIRCLE.

from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def is_inside_circle(px, py, cx, cy, r):
            return (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2
        
        answer = []
        for cx, cy, r in queries:
            count = 0
            for px, py in points:
                if is_inside_circle(px, py, cx, cy, r):
                    count += 1
            answer.append(count)
        
        return answer

points = [[1, 3], [3, 3], [5, 3], [2, 2]]
queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
solution = Solution()
output = solution.countPoints(points, queries)
print(output)  
>>>>>>> 7b7328341ea8bd86372e5cf8b7dd65a33e5eb4cb
