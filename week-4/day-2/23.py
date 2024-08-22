# Merge K sorted Lists.

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, idx, l))
        
        dummy = ListNode()
        current = dummy
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

solution = Solution()
merged_list = solution.mergeKLists(lists)
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

print(linked_list_to_list(merged_list)) 
