# Split Linked List in Parts.

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # Step 1: Count the total number of nodes in the list
        total_length = 0
        current = head
        while current:
            total_length += 1
            current = current.next
        # Step 2: Calculate the size of each part.
        part_size, extra_nodes = divmod(total_length, k)
        
        # Step 3: Initialize the result list to store the head of each part
        result = []
        current = head
        
        for i in range(k):
            # Step 4: Start a new part and assign its head
            part_head = current
            result.append(part_head)
            
            # Step 5: Determine the size of the current part
            current_part_size = part_size + (1 if i < extra_nodes else 0)
            
            # Step 6: Traverse the current part
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            # Step 7: Break the link if the part is non-empty
            if current:
                next_part = current.next
                current.next = None
                current = next_part
        
        return result
