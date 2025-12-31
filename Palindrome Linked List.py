class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # For odd length, skip the middle node
        if fast:
            slow = slow.next

        second = self.reverse(slow)
        first = head

        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next

        return True

    def reverse(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev

''' 
    time complexity : O(n)
    space complexity : O(1)
'''
