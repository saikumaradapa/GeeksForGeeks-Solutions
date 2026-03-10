class Solution:
    def countSubarrays(self, arr):
        
        n = len(arr)
        stack = []
        next_smaller = [n] * n
        
        for i in range(n):
            
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                next_smaller[idx] = i
            
            stack.append(i)
        
        total = 0
        
        for i in range(n):
            total += next_smaller[i] - i
        
        return total
