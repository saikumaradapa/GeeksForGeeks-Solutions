# 1. Brute force approach

class Solution:
    def segregate(self, head):
        """
        - Counts the number of 0s, 1s, and 2s
        - Overwrites node data in two passes
        
        Time Complexity: O(n) -- two passes over the list
        Space Complexity: O(1) -- no extra space beyond counters
        """
        curr = head
        zeros, ones, twos = 0, 0, 0
        while curr:
            if curr.data == 0:
                zeros += 1
            elif curr.data == 1:
                ones += 1
            else:
                twos += 1
            curr = curr.next 
        
        curr = head
        while curr:
            if zeros:
                curr.data = 0
                zeros -= 1
            elif ones:
                curr.data = 1
                ones -= 1
            else:
                curr.data = 2
                twos -= 1
            curr = curr.next 
        return head

#############################################################################################################################################################################################

# 2. Optimal approach

class SolutionOptimal:
    def segregate(self, head):
        """
        - Uses dummy head/tail nodes to create separate lists for 0s, 1s, and 2s
        - Merges them at the end (preserves original node objects)
        
        Time Complexity: O(n) -- single pass over the list
        Space Complexity: O(1) -- uses only pointer variables
        """
        if not head or not head.next:
            return head

        # Dummy heads and tails for 0s, 1s, 2s
        zero_head = zero_tail = Node(0)
        one_head = one_tail = Node(0)
        two_head = two_tail = Node(0)

        curr = head
        while curr:
            if curr.data == 0:
                zero_tail.next = curr
                zero_tail = zero_tail.next
            elif curr.data == 1:
                one_tail.next = curr
                one_tail = one_tail.next
            else:  # curr.data == 2
                two_tail.next = curr
                two_tail = two_tail.next
            curr = curr.next

        # Connect 0s → 1s → 2s
        zero_tail.next = one_head.next if one_head.next else two_head.next
        one_tail.next = two_head.next
        two_tail.next = None

        return zero_head.next
