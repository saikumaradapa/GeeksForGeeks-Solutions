class Solution:
    def compute(self, head):
        head = self.reverse(head)
        curr = head
        while curr and curr.next:
            if curr.next.data < curr.data:
                curr.next = curr.next.next  # remove smaller node
            else:
                curr = curr.next
        return self.reverse(head)

    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

'''
    reverse, then after reversal head is the max
    remove any node smaller than its predecessor (which is the running max)
    reverse back
    same complexity, slightly fewer variables
    time complexity : O(n)
    space complexity : O(1)
'''

##################################################################################################################################################


class Solution:
    def compute(self, head):
        curr = self.reverse(head)
        prev_val = 0
        tail = dummy = Node(0)
        while curr:
            if prev_val <= curr.data:
                tail.next = curr
                curr = curr.next
                tail = tail.next
                tail.next = None
                prev_val = tail.data
                continue
            curr = curr.next
        return self.reverse(dummy.next)

    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

'''
    reverse list → now "greater to right" becomes "greater to left"
    scan left to right keeping running max (prev_val)
    keep only nodes >= running max (non-decreasing from left)
    reverse again to restore original order
    time complexity : O(n)
    space complexity : O(1)
'''
