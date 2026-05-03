from collections import defaultdict
class Solution:
    def sortBySetBitCount(self, arr):
        def get_bit_cnt(n):
            cnt = 0
            for i in range(33):
                cnt += (n >> i) & 1
            return cnt

        bucket = defaultdict(list)
        for n in arr:
            bucket[get_bit_cnt(n)].append(n)

        idx = 0
        for i in range(32, -1, -1):
            for n in bucket[i]:
                arr[idx] = n
                idx += 1
        return arr

'''
    bucket sort by set bit count
    iterate buckets from highest to lowest
    stable since elements within each bucket maintain original order
    time complexity : O(n)
    space complexity : O(n)
'''

#################################################################################

class Solution:
    def sortBySetBitCount(self, arr):
        arr.sort(key=lambda x: -bin(x).count('1'))
        return arr

'''
    sort descending by set bit count
    Python's sort is stable, so equal bit counts keep original order
    bin(x).count('1') gives set bit count
    time complexity : O(n log n)
    space complexity : O(1)
'''


