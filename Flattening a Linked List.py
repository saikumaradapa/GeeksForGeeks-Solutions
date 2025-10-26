# Approach 2: Min-Heap (Priority Queue Merge of K Sorted Lists)
import heapq

class Solution:
    def flatten(self, root):
        """
        Time Complexity: O(T * log N)    # N = number of head nodes, T = total number of nodes across all sublists.
        Space Complexity: O(N)
        """
        if not root:
            return None
        
        heap = []
        node = root
        while node:
            heapq.heappush(heap, (node.data, node))
            node = node.next
        
        dummy = Node(-1)
        curr = dummy
        
        while heap:
            val, node = heapq.heappop(heap)
            curr.bottom = node
            curr = curr.bottom
            if node.bottom:
                heapq.heappush(heap, (node.bottom.data, node.bottom))
            node.next = None  # Avoid confusion, keep list single-level
        
        return dummy.bottom



#################################################################################################################################################################################

# Approach 1: Recursive Merge (Pairwise Merge of Bottom Lists)
class Solution:
    def flatten(self, root):
        """
        Time Complexity: O(N * M) # N = number of head nodes and M = average number of nodes in each sublist.
        Space Complexity: O(N) # due to recursion stack
        """
        if not root:
            return root
        
        mergedHead = self.flatten(root.next)
        
        root.next = None
        curr = dummy = Node(-1)
        while root and mergedHead:
            if root.data <= mergedHead.data:
                curr.bottom = root
                root = root.bottom
            else:
                curr.bottom = mergedHead
                mergedHead = mergedHead.bottom
            curr = curr.bottom
        if root:
            curr.bottom = root
        if mergedHead:
            curr.bottom = mergedHead
        return dummy.bottom
