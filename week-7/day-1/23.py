# MERGE K SORTED LISTS.

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # Create a min-heap (priority queue)
        min_heap = []
        
        # Initialize the heap with the head nodes of each linked list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))  # (value, index, node)
        
        # Create a dummy node to help with result list construction
        dummy = ListNode()
        current = dummy
        
        # While the heap is not empty, process the nodes
        while min_heap:
            val, i, node = heapq.heappop(min_heap)  # Get the smallest node
            current.next = node  # Add the node to the result list
            current = current.next  # Move to the next node
            
            # If there are more nodes in the same list, add the next node to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        # Return the merged list (starting from dummy.next)
        return dummy.next

# Example Usage
# Input: lists = [[1,4,5],[1,3,4],[2,6]]

# Create the individual linked lists
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]

# Call the solution
solution = Solution()
merged_head = solution.mergeKLists(lists)

# Print the merged linked list
while merged_head:
    print(merged_head.val, end=" -> " if merged_head.next else "\n")
    merged_head = merged_head.next
