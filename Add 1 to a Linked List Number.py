# 1. recursion approach 

class Solution:
    def addOne(self, head: 'Node') -> 'Node':
        """
        Time Complexity: O(n)
        Space Complexity: O(n) (due to recursion stack)
        """

        def add_with_carry(node: 'Node') -> int:
            if not node:
                return 1  # Initial carry (adding 1) | Base case
            carry = add_with_carry(node.next)
            total = node.data + carry
            node.data = total % 10
            return total // 10

        carry = add_with_carry(head)
        if carry:
            new_head = Node(1)
            new_head.next = head
            return new_head
        return head
