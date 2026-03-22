class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        ans = [0] * n
        
        index_map = {v: i for i, v in enumerate(arr)}
        arr.sort()
        
        # Precompute Catalan numbers
        catalan = [0] * (n + 1)
        catalan[0] = 1
        catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        for i in range(n):
            left = i
            right = n - i - 1
            root_value = arr[i]
            original_index = index_map[root_value]
            
            ans[original_index] = catalan[left] * catalan[right]
        
        return ans


''' catalan sequence 

    time complexity : O(n log n) + O(n^2) = O(n log n)   ( since n ≤ 6 )
    space complexity : O(n)

notes : 
1) Define f(n) = number of BSTs with n nodes
2) Recurrence:
   f(n) = Σ f(i) * f(n-i-1)

3) For each element as root:
   left = count of smaller elements
   right = count of larger elements

4) answer[root] = catalan[left] * catalan[right]

5) Pattern recognition:
   - pick root
   - split into left & right
   - multiply independent choices
   - sum over all possible roots
   → Catalan pattern
'''
