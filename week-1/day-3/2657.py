# FIND THE PREFIX COMMON ARRAY OF TWO ARRAYS

class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        seen_in_A = set()
        seen_in_B = set()
        C = []

        for i in range(n):
            seen_in_A.add(A[i])
            seen_in_B.add(B[i])
            common_count = len(seen_in_A & seen_in_B)
            C.append(common_count)

        return C


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
solution = Solution()
print(solution.findThePrefixCommonArray(A, B))  
