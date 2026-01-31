class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)
        if n <= 1:
            return 0.0

        # max initial gap
        high = max(stations[i+1] - stations[i] for i in range(n-1))
        low = 0.0

        while high - low > 1e-6:
            mid = (low + high) / 2
            print(mid)
            if self.can_achieve(stations, k, mid):
                high = mid
            else:
                low = mid

        return round(high, 6)

    def can_achieve(self, stations, k, d):
        needed = 0
        for i in range(len(stations) - 1):
            gap = stations[i+1] - stations[i]
            needed += int(gap / d)
            # if too many already, stop early
            if needed > k:
                return False
        return needed <= k

''' binary search on answers  
    time complexity : O(nlog(range/precision​)) ≈ O(n)
    space complexity : O(1)
'''

#######################################################################################################################################################################################################


from heapq import heappush, heappop

class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)
        if n <= 1:
            return 0.0

        # Max heap: (-current_gap, parts, index)
        heap = []

        for i in range(n - 1):
            gap = stations[i + 1] - stations[i]
            heappush(heap, (-gap, 1, i))

        for _ in range(k):
            neg_gap, parts, idx = heappop(heap)
            parts += 1
            original_gap = stations[idx + 1] - stations[idx]
            new_gap = original_gap / parts
            heappush(heap, (-new_gap, parts, idx))

        return -heap[0][0]

''' using max heap | priority queue  
    time complexity : O(k logn)
    space complexity : O(n)
'''

#######################################################################################################################################################################################################

class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)
        if n <= 1:
            return 0.0

        # extra_stations[i] = number of extra stations added between stations[i] and stations[i+1]
        extra_stations = [0] * (n - 1)

        # Add k stations one by one
        for _ in range(k):
            max_gap = -1.0
            max_gap_index = -1

            for i in range(n - 1):
                gap = stations[i + 1] - stations[i]
                current_max_gap = gap / (extra_stations[i] + 1)

                if current_max_gap > max_gap:
                    max_gap = current_max_gap
                    max_gap_index = i

            extra_stations[max_gap_index] += 1

        # Compute the final maximum distance
        answer = 0.0
        for i in range(n - 1):
            gap = stations[i + 1] - stations[i]
            answer = max(answer, gap / (extra_stations[i] + 1))

        return answer

''' brute force aporach 
    time complexity : O(n * k)
    space complexity : O(n)
'''
