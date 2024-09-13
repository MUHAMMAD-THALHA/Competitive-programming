# XOR Queries of a Subarray.

class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # Step 1: Compute prefix XOR
        prefix_xor = [0] * (len(arr) + 1)
        
        for i in range(1, len(arr) + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
        
        # Step 2: Answer each query
        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return result
