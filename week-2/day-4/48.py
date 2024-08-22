# Rotate Image.

class Solution:
    def rotate(self, matrix):
        """
        Rotates the n x n matrix by 90 degrees clockwise in-place.
        
        Args:
        matrix (List[List[int]]): 2D list representing the n x n matrix.
        
        Returns:
        None: The function modifies the matrix in place.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

# Output:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print(matrix)  
