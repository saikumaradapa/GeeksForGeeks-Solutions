class Solution:
    def kokoEat(self, piles, h):
        l, r = 1, max(piles) 
        while l <= r:
            mid = (l + r) // 2
            if self.possible(piles, mid, h):
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans
    
    def possible(self, piles, k, h):
        total_hours = 0
        for i in range(len(piles)):
            total_hours += piles[i] // k
            total_hours += 1 if piles[i] % k else 0
        return total_hours <= h
        
''' binary search  
    time complexity : O(n log(max(piles)))
    space complexity : O(1)
'''
