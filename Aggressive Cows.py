class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        
        low, high = 1, stalls[-1] - stalls[0]  
        result = 0
        
        while low <= high:
            mid = (low + high) // 2  
            
            if self.canPlaceCows(stalls, k, mid):
                result = mid  
                low = mid + 1  # Try for a larger distance
            else:
                high = mid - 1  # Try for a smaller distance
        
        return result



    def canPlaceCows(self, stalls, k, min_dist):
        count = 1  # Place the first cow in the first stall
        last_position = stalls[0]  # Track the position of the last cow placed
        
        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= min_dist:
                count += 1  # Place the next cow
                last_position = stalls[i]  # Update the last position
            if count >= k:  # All cows are placed successfully
                return True
        
        return False  # Not all cows can be placed
        
''' binary search max of min approach 
    time complexity : O(n logm)
    space complexity : O(1)
'''
