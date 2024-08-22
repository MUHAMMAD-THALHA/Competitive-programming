# Add Two Numbers.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Adds two numbers represented by linked lists.
        
        Args:
        l1 (ListNode): Head of the first linked list.
        l2 (ListNode): Head of the second linked list.
        
        Returns:
        ListNode: Head of the resulting linked list that represents the sum.
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2:
           
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
           
            total = val1 + val2 + carry
            carry = total // 10  
            new_val = total % 10  
            
            current.next = ListNode(new_val)
            current = current.next
          
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next  

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = Solution().addTwoNumbers(l1, l2)

output = []
while result:
    output.append(result.val)
    result = result.next

print(output)  
