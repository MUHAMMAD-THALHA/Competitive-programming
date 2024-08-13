#NUMBER OF RECTANGLES THAT FORM LARGEST SQUARE

class Solution:
    def countGoodRectangles(self, rectangles):
        max_len = 0
        count = 0
        
        for l, w in rectangles:
            square_side = min(l, w)
            if square_side > max_len:
                max_len = square_side
                count = 1
            elif square_side == max_len:
                count += 1
        
        return count
rectangles = [[5,8],[3,9],[5,12],[16,5]]
solution = Solution()
print(solution.countGoodRectangles(rectangles))  
