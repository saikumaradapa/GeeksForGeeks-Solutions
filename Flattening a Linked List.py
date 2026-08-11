# Approach 1: Recursive Merge (Right-to-Left Pairwise Merge)

class Solution:
    def flatten(self, root):
        """
        Time Complexity: O(M * N²)
            - Each merge is O(accumulated_length + M)
            - Work: 2M + 3M + 4M + ... + NM = O(M * N²)

        Space Complexity: O(N)
            - Recursion stack depth = N (number of head nodes)

        Approach: Recurse to the rightmost list first, then merge backwards.
                  Each call merges current list with the already-flattened right portion.
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

# Approach 2: Min-Heap (Merge K Sorted Lists)

import heapq

class Solution:
    def flatten(self, root):
        """
        Time Complexity: O(T * log N) = O(N * M * log N)
            - Every node is pushed and popped exactly once → T operations
            - Each push/pop costs O(log N) since heap size ≤ N

        Space Complexity: O(N)
            - Heap never exceeds N entries (one per head list)

        Approach: Push all N head nodes into a min-heap. Pop smallest, attach to result,
                  push its bottom child. Repeat until heap is empty.
                  Classic "merge K sorted lists" pattern.
        """
        if not root:
            return None

        heap = []
        idx = 0
        node = root
        while node:
            heapq.heappush(heap, (node.data, idx, node))
            idx += 1
            node = node.next

        dummy = Node(-1)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.bottom = node
            curr = curr.bottom
            if node.bottom:
                heapq.heappush(heap, (node.bottom.data, idx, node.bottom))
                idx += 1
            node.next = None

        return dummy.bottom

# Approach 3: Iterative Merge (Left-to-Right Pairwise Merge)

class Solution:
    def flatten(self, root):
        """
        Time Complexity: O(M * N²)
            - Each merge is O(accumulated_length + M)
            - Work: 2M + 3M + 4M + ... + NM = O(M * N²)

        Space Complexity: O(1)
            - No recursion, no extra data structures, just pointer manipulation

        Approach: Start with first list. Merge it with the second, then merge result
                  with the third, and so on left-to-right. Same as Approach 1 but
                  iterative — saves recursion stack space.
        """
        prev_head = root
        curr_head = root.next
        prev_head.next = None

        while curr_head:
            next_head = curr_head.next
            curr_head.next = None
            prev_head = self.merge(prev_head, curr_head)
            curr_head = next_head

        return prev_head

    def merge(self, l1, l2):
        d = curr = Node(-1)
        while l1 and l2:
            if l1.data <= l2.data:
                curr.bottom = l1
                l1 = l1.bottom
            else:
                curr.bottom = l2
                l2 = l2.bottom
            curr = curr.bottom
        if l1:
            curr.bottom = l1
        if l2:
            curr.bottom = l2
        return d.bottom
