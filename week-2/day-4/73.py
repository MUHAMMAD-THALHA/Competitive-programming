# Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix):
        """
        Modifies the matrix in-place to set entire rows and columns to 0
        if an element in the matrix is 0.
        
        Args:
        matrix (List[List[int]]): 2D list representing the matrix.
        
        Returns:
        None: The function modifies the matrix in place.
        """
        
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

# Output:
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution().setZeroes(matrix)
print(matrix) 
