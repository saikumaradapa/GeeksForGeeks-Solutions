class Solution:
    def permuteDist(self, arr):
        res = []
        
        def backtrack(start):
            # If we fixed all positions
            if start == len(arr):
                res.append(arr[:])   # copy current permutation
                return
            
            for i in range(start, len(arr)):
                # Swap to place element at current position
                arr[start], arr[i] = arr[i], arr[start]
                
                backtrack(start + 1)
                
                # Backtrack (restore array)
                arr[start], arr[i] = arr[i], arr[start]
        
        backtrack(0)
        return res
