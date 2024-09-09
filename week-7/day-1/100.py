# SAME TREE

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both trees are empty, they are the same
        if not p and not q:
            return True
        # One of the trees is empty, they are not the same
        if not p or not q:
            return False
        # The current nodes have different values
        if p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
# Tree p = [1,2,3]
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Tree q = [1,2,3]
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

solution = Solution()
result = solution.isSameTree(p, q)
print(result)  
