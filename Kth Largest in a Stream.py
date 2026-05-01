class Solution:
    def kthLargest(self, arr, k):
        from heapq import heappush, heappushpop
        heap = []
        ans = []
        for n in arr:
            if len(heap) < k:
                heappush(heap, n)
            else:
                heappushpop(heap, n)
            if len(heap) < k:
                ans.append(-1)
            else:
                ans.append(heap[0])
        return ans

'''
    maintain a min-heap of size k
    heap[0] is always the kth largest element
    if heap has fewer than k elements, answer is -1
    time complexity : O(n * log(k))
    space complexity : O(k)
'''
