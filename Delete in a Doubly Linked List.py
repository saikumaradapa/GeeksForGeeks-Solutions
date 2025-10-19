class Solution:
    def delPos(self, head, x):
        """
        Deletes the node at position x (1-based) from a doubly linked list.
        
        Parameters:
        head (Node): Head node of the doubly linked list.
        x (int): Position (1-indexed) of the node to delete.
        
        Returns:
        Node: The updated head of the list after deletion.
        Time Complexity: O(n)
        Auxiliary Space: O(1)
        """
        if not head:
            return None
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            head.next = None
            return new_head
        curr = head
        for _ in range(x - 1):
            curr = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next
        curr.prev = None
        curr.next = None
        return head
