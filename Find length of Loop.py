class SolutionFloyd:
    def countNodesInLoop(self, head: ListNode) -> int:
        """
        # tortoise and hare algorithm, also known as Floyd's cycle-finding algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Loop detected
            if slow == fast:
                return self.count_loop_length(slow)

        return 0  # No loop

    def count_loop_length(self, node_in_loop: ListNode) -> int:
        count = 1
        current = node_in_loop.next
        while current != node_in_loop:
            count += 1
            current = current.next
        return count


##############################################################################################################################################################

class SolutionHashMap:
    def lengthOfLoop(self, head: ListNode) -> int:
        """
        # with help of hasMap
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head or not head.next:
            return 0
        
        timer = 1
        mem = dict()
        curr = head
        while curr:
            if curr in mem:
                return timer - mem[curr]
            mem[curr] = timer
            timer += 1
            curr = curr.next
        return 0
