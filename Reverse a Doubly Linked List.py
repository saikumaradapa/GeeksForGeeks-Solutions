class Solution:
    def reverse(self, head):
        """
        1. Two-pointer (swap data) Approach
        
        Time Complexity: O(n) -- Each node's data is swapped once.
        Space Complexity: O(1) -- No extra space is used apart from variables.
        """
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next 
        
        curr = head
        for _ in range(n // 2):
            curr.data, tail.data = tail.data, curr.data
            curr = curr.next 
            tail = tail.prev 
        
        return head
      
###########################################################################################################################################################################

class Solution:
    def reverse(self, head):
        """
        2. Single-iteration pointer change
        
        Time Complexity: O(n) -- Each node is visited once.
        Space Complexity: O(1) -- No extra space is used.
        """
        if not head or not head.next:
            return head
        
        curr = head
        while curr:
            last = curr.prev
            curr.prev = curr.next 
            curr.next = last
            curr = curr.prev
        
        return last.prev

###########################################################################################################################################################################

class Solution:
    def reverse(self, head):
        """
        3. Recursion Approach
        
        Time Complexity: O(n) -- Each node is visited once.
        Space Complexity: O(n) -- Recursion stack for n nodes.
        """
        if not head or not head.next:
            return head
        
        newHead = self.reverse(head.next)
        nextNode = head.next 
        nextNode.next = head
        head.prev = nextNode 
        head.next = None 
    
        return newHead
