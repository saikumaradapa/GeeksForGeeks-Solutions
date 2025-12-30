class Solution:
    def addTwoLists(self, num1, num2):
        l1 = self.reverse(num1)
        l2 = self.reverse(num2)

        dummy = Node(-1)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.data
                l1 = l1.next
            if l2:
                total += l2.data
                l2 = l2.next

            curr.next = Node(total % 10)
            carry = total // 10
            curr = curr.next

        result = self.reverse(dummy.next)

        # Remove leading zeros
        while result and result.data == 0:
            result = result.next

        return result if result else Node(0)
        
    def reverse(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
        
        
''' 
    time complexity : O(n + m)
    space complexity : O(1)
'''
