# Insert Greatest Common Divisiors in Linked List.

import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            gcd_value = math.gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            new_node = ListNode(gcd_value)
            
            # Insert the new node between current and next node
            new_node.next = current.next
            current.next = new_node
            
            # Move current to the node after the inserted node
            current = new_node.next
        
        return head
