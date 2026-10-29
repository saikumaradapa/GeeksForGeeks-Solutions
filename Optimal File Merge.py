import heapq

class Solution:
    def minComputation(self, files):

        if len(files) <= 1:
            return 0                     # nothing to merge

        heap = files[:]                  # copy so the input isn't modified
        heapq.heapify(heap)
        total = 0

        while len(heap) > 1:
            a = heapq.heappop(heap)      # smallest
            b = heapq.heappop(heap)      # second smallest
            merged = a + b
            total += merged              # cost of this merge
            heapq.heappush(heap, merged) # the merged file can be merged again

        return total
