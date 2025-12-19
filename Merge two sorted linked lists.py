Problem Link : https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1


class Solution:
    def sortedMerge(self,head1, head2):
        new_head = dummy = Node(-1)
        
        while head1 and head2:
            if head1.data <= head2.data:
                dummy.next = head1
                head1 = head1.next 
            else:
                dummy.next = head2
                head2 = head2.next                 
            dummy = dummy.next 
        
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
    
        return new_head.next 

''' time complexity : O(n + m)
    space complexity : O(1)
'''
