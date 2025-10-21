# 1. using heapq

from collections import defaultdict, Counter
import heapq

class SolutionHeap:
    def topKFreq(self, arr: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n + m log m), where n = len(arr), m = #unique elements.
        Space Complexity: O(m), for frequency map and heap.
        Best Use Case : k << m; need only top k elements
        """
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1

        min_heap = [(-count, -num) for num, count in freq.items()]
        heapq.heapify(min_heap)

        result = []
        for _ in range(k):
            result.append(-heapq.heappop(min_heap)[1])
        return result

######################################################################################################################################################################

# 2. using lambda as key in sorted

class SolutionSort:
    def topKFreq(self, arr: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n log n), where n = #unique elements.
        Space Complexity: O(m), where m = #unique elements.
        Best Use Case : Need all elements sorted by freq
        """
        freq = Counter(arr)
        sorted_items = sorted(
            freq.items(),
            key=lambda x: (x[1], x[0]),
            reverse=True
        )
        return [item[0] for item in sorted_items[:k]]
