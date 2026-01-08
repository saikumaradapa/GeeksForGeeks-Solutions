class Solution:
    def countSubarrays(self, arr, k):
        return self.atMost(arr, k) - self.atMost(arr, k - 1)

    def atMost(self, arr, k):
        left = 0
        odd_count = 0
        res = 0

        for right in range(len(arr)):
            if arr[right] % 2 == 1:
                odd_count += 1

            while odd_count > k:
                if arr[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            res += right - left + 1

        return res

''' count subarrays with atmost k odds 
    time complexity : O(n)
    space complexity : O(1)
'''

####################################################################################################################################################################################################

class Solution:
    def countSubarrays(self, arr, k):
        res = 0
        odd = 0

        l, m = 0, 0
        for r in range(len(arr)):
            if arr[r] % 2:
                odd += 1
            
            while odd > k:
                if arr[l] % 2:
                    odd -= 1                    
                l += 1
                m = l 

            if odd == k:
                while not arr[m] % 2:
                    m += 1
                res += m - l + 1
            
        return res
        
''' three pointers approach 
    time complexity : O(n)
    space complexity : O(1)
'''

####################################################################################################################################################################################################

class Solution:
    def countSubarrays(self, arr, k):
        n = len(arr)

        # prefix[i] = index of previous odd before i
        prefix = [-1] * n
        last_odd = -1
        for i in range(n):
            prefix[i] = last_odd
            if arr[i] % 2 == 1:
                last_odd = i

        # suffix[i] = index of next odd after i
        suffix = [n] * n
        last_odd = n
        for i in range(n - 1, -1, -1):
            suffix[i] = last_odd
            if arr[i] % 2 == 1:
                last_odd = i

        # Find first odd
        l = suffix[0] if arr[0] % 2 == 0 else 0
        r = l

        # Move r to k-th odd
        for _ in range(k - 1):
            if r >= n:
                return 0
            r = suffix[r]

        res = 0
        while r < n:
            left_choices = l - prefix[l]
            right_choices = suffix[r] - r
            res += left_choices * right_choices

            l = suffix[l]
            r = suffix[r]

        return res

''' prefix count and two pointer approach 
    time complexity : O(n)
    space complexity : O(n)
'''
