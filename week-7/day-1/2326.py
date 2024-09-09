# SPIRAL MATRIX IV

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        # Step 1: Initialize the m x n matrix with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Step 2: Define the boundaries for the spiral traversal
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Step 3: Start the traversal
        current = head
        while top <= bottom and left <= right and current:
            # Traverse from left to right on the top row
            for j in range(left, right + 1):
                if current:
                    matrix[top][j] = current.val
                    current = current.next
            top += 1
            
            # Traverse from top to bottom on the right column
            for i in range(top, bottom + 1):
                if current:
                    matrix[i][right] = current.val
                    current = current.next
            right -= 1
            
            # Traverse from right to left on the bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if current:
                        matrix[bottom][j] = current.val
                        current = current.next
                bottom -= 1
            
            # Traverse from bottom to top on the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if current:
                        matrix[i][left] = current.val
                        current = current.next
                left += 1
        
        return matrix
